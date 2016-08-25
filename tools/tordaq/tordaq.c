#include <unistd.h> 
#include <stdio.h>
#include <vector>

#include <TSystem.h>
#include <TNtupleD.h>

#include "tordaq.h"

Double_t getTime(Long64_t sec,Long64_t nsec,Int_t wflength,Int_t nsample)
{
    nsec += nsample*((Long64_t)1e9)/wflength;
    const Long64_t extrasec=nsec/1e9;
    const Long64_t extransec=nsec%(Long64_t)1e9;
    sec += extrasec;
    return sec + extransec/1e9;
}

int main(int argc,char **argv)
{
    const char* separator=",";
    TString inFilename="torus.root";
    TString outAsciiFilename="";
    TString outRootFilename="";
    Long64_t maxSamples=-1;
    Long64_t startTime=-1;
    Long64_t endTime=-1;

    TString usage="\ntordaq2txt -i inputFilename [options]\n"
        "\t  [-o output ascii filename]\n"
        "\t  [-t output ROOT filename]\n"
        "\t  [-s first second]\n"
        "\t  [-e last second]\n"
        "\t  [-n max # samples]\n"
        "\t  [-h]\n";
   
    int itmp;
    while ( (itmp=getopt(argc,argv,"i:o:t:s:e:n:h")) != -1 )
    {
        switch (itmp)
        {
            case 'i':
                inFilename=optarg;
                break;
            case 'o':
                outAsciiFilename=optarg;
                break;
            case 't':
                outRootFilename=optarg;
                break;
            case 's':
                startTime=atoi(optarg);
                break;
            case 'e':
                endTime=atoi(optarg);
                break;
            case 'n':
                maxSamples=atoi(optarg);
                break;
            case 'h':
                std::cout<<usage<<std::endl;
                exit(0);
            default:
                std::cout<<usage<<std::endl;
                exit(1);
        }
    }

    if (gSystem->AccessPathName(inFilename))
    {
        std::cerr<<"Input File Does Not Exist:  "<<inFilename<<std::endl;
        exit(1);
    }
    if (outAsciiFilename!="" && !gSystem->AccessPathName(outAsciiFilename))
    {
        if (outAsciiFilename!="stdout")
        {
            std::cerr<<"Output File Already Exists:  "<<outAsciiFilename<<std::endl;
            exit(1);
        }
    }
    if (outRootFilename!="" && !gSystem->AccessPathName(outRootFilename))
    {
        std::cerr<<"Output File Already Exists:  "<<outRootFilename<<std::endl;
        exit(1);
    }

    std::vector <bool> skipVars;
    std::vector <tordaq*> tordaqs;
    TFile *inFile=new TFile(inFilename,"READ");
    int itree=1;
    while (1)
    {
        TTree *tt=(TTree*)inFile->Get(Form("VT%d",itree++));
        if (tt)
        {
            tordaqs.push_back(new tordaq(tt));
            skipVars.push_back(false);
        }
        else break;
    }

    if (tordaqs.size()<1)
    {
        std::cerr<<"Found No Trees"<<std::endl;
        exit(1);
    }
    
    std::cout<<"Found "<<tordaqs.size()<<" Variables."<<std::endl;
    
    FILE *outAsciiFile=NULL;
    if (outAsciiFilename=="stdout") outAsciiFile=stdout;
    else if (outAsciiFilename!="")  outAsciiFile=fopen(outAsciiFilename,"w");
    
    TNtupleD *outTree=NULL;
    TFile *outRootFile=NULL;
    if (outRootFilename!="")
    {
        TString vars="t1:x1";
        for (unsigned int ii=1; ii<tordaqs.size(); ii++)
            vars+=Form(":t%d:x%d",ii+1,ii+1);
        outRootFile=new TFile(outRootFilename,"CREATE");
        outTree=new TNtupleD("tordaq","",vars);
    }

    Long64_t jentry=-1;
    Long64_t nSamples=0;
    Double_t vars[1000];

    while (1)
    {
        jentry++;

        bool allEarly=1;
        bool allLate=1;

        for (unsigned int iVar=0; iVar<tordaqs.size(); iVar++)
        {
            skipVars[iVar]=false;
            if (tordaqs[iVar]->LoadTree(jentry) < 0) skipVars[iVar]=true;
            else
            {
                tordaqs[iVar]->fChain->GetEntry(jentry);
                const Double_t time = getTime(tordaqs[iVar]->record_tsec,
                                              tordaqs[iVar]->record_tnsec,
                                              tordaqs[iVar]->WFLENGTH,
                                              0);
                if (endTime<0   || time < endTime) allLate=0;
                if (startTime<0 || time > startTime) allEarly=0;
            }
        }
       
        if (allLate) break;
        if (allEarly) continue;

        for (int iSamp=0; iSamp<tordaqs[0]->WFLENGTH; iSamp++)
        {
            char sep[1]="";
            for (unsigned int iVar=0; iVar<tordaqs.size(); iVar++)
            {
                Double_t time=0,data=0;
                vars[2*iVar]=vars[2*iVar+1]=0;
                if (!skipVars[iVar])
                {
                    data = tordaqs[iVar]->record_data[iSamp];
                    time = getTime(tordaqs[iVar]->record_tsec,
                                   tordaqs[iVar]->record_tnsec,
                                   tordaqs[iVar]->WFLENGTH,
                                   iSamp);
                    vars[2*iVar]=time;
                    vars[2*iVar+1]=data;
                }
                if (outAsciiFile)
                    fprintf(outAsciiFile,"%s%18.4f%s%12f",sep,time,separator,data);
                strcpy(sep,separator);
            }
            if (outAsciiFile) fprintf(outAsciiFile,"\n");
            if (outTree) outTree->Fill(vars);
            if (++nSamples>=maxSamples && maxSamples>0) break;
        }
    }
    
    if (outAsciiFile) fclose(outAsciiFile);
    if (outRootFile) 
    {
        if (outTree) outTree->AutoSave();
        outRootFile->Close();
    }
}

