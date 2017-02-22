#include <unistd.h> 
#include <stdio.h>
#include <string>
#include <time.h>

#include <TSystem.h>
#include <TH1.h>

#include "tordaqReader.hh"

int main(int argc,char **argv)
{
    TString usage="\ntordaqConverter [options]\n"
        "\t  -i input wf2root filename\n"
        "\t  -o output ascii filename\n"
        "\t  -t output ROOT filename with ntuple\n"
        "\t  -H output ROOT filename with histos\n"
        "\t  -s first epoch second or YYYY-MM-DD_HH:MM:SS\n"
        "\t  -e last  epoch second or YYYY-MM-DD_HH:MM:SS\n"
        "\t  -n max # samples\n"
        "\t  -R (output Ruben's ascii time format)\n"
        "\t  -S (force synchronization)\n"
        "\t  -h (print usage)\n";
   
    const char* timeFormat="%Y-%m-%d_%H:%M:%S";

    tordaqReader tdr;
   
    int itmp;
    std::string sStartTime="";
    std::string sEndTime="";
    
    while ( (itmp=getopt(argc,argv,"i:o:t:s:e:H:n:RSh")) != -1 )
    {
        switch (itmp)
        {
            case 'i':
                tdr.inFilename=optarg;
                break;
            case 'o':
                tdr.outAsciiFilename=optarg;
                break;
            case 't':
                tdr.outRootFilename=optarg;
                tdr.makeNtuple=true;
                break;
            case 'H':
                tdr.outRootFilename=optarg;
                tdr.makeHistos=true;
                break;
            case 's':
                sStartTime=optarg;
                break;
            case 'e':
                sEndTime=optarg;
                break;
            case 'n':
                tdr.maxSamples=std::stoi(optarg);
                break;
            case 'R':
                tdr.rubenTime=true;
                break;
            case 'S':
                tdr.forceSynchro=true;
                break;
            case 'h':
                std::cout<<usage<<std::endl;
                exit(0);
            default:
                std::cout<<"Invalid Argument:  -"<<itmp<<std::endl;
                std::cout<<usage<<std::endl;
                exit(1);
        }
    }

    // interpret start time argument:
    if (sStartTime!="")
    {
        if (sStartTime.find(":")==std::string::npos)
            tdr.startTime=std::stoi(sStartTime.c_str());
        else
        {
            struct tm tm;
            strptime(sStartTime.c_str(),timeFormat,&tm);
            tdr.startTime=mktime(&tm);
        }
        std::cout<<"Start Time:  "<<tdr.startTime<<std::endl;
    }
    
    // interpret end time argument:
    if (sEndTime!="")
    {
        if (sEndTime.find(":")==std::string::npos)
            tdr.endTime=std::stoi(sEndTime.c_str());
        else
        {
            struct tm tm;
            strptime(sEndTime.c_str(),timeFormat,&tm);
            tdr.endTime=mktime(&tm);
        }
        std::cout<<"End Time:    "<<tdr.endTime<<std::endl;
    }

    if (tdr.endTime>0 && tdr.startTime>0)
    {
        if (tdr.endTime < tdr.startTime)
        {
            std::cerr<<"User Error:  Start Time later then End Time."<<std::endl;
            exit(1);
        }
    }

    // check filesystem for input file:
    if (gSystem->AccessPathName(tdr.inFilename))
    {
        std::cerr<<"Input File Does Not Exist:  "<<tdr.inFilename<<std::endl;
        std::cerr<<usage<<std::endl;
        exit(1);
    }

    // check filesystem for output files:
    if (tdr.outAsciiFilename!="" && !gSystem->AccessPathName(tdr.outAsciiFilename))
    {
        if (tdr.outAsciiFilename!="stdout")
        {
            std::cerr<<"Output File Already Exists:  "<<tdr.outAsciiFilename<<std::endl;
            std::cerr<<usage<<std::endl;
            exit(1);
        }
    }
    if (tdr.outRootFilename!="" && !gSystem->AccessPathName(tdr.outRootFilename))
    {
        std::cerr<<"Output File Already Exists:  "<<tdr.outRootFilename<<std::endl;
        std::cerr<<usage<<std::endl;
        exit(1);
    }

    // the real work:
    if (!tdr.process()) exit(1);

    std::cout<<std::endl<<"Closing Files ..."<<std::endl<<std::endl;
    
    if (tdr.outRootFile) 
    {
        if (tdr.outTree) tdr.outTree->AutoSave();

        // this is slow:
        if (tdr.makeHistos) 
        {
            std::cout<<std::endl<<"Writing Histograms ... (this can take a couple minutes) ..."<<std::endl<<std::endl;
            tdr.WriteRemainingHistos();
        }

        tdr.outRootFile->Close();
    }
}


