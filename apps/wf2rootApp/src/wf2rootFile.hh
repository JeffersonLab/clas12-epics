/*
 * wf2rootFile.hh
 *
 *  Created on: Mar 24, 2014
 *      Author: yqiang
 */

#ifndef WF2ROOTFILE_HH_
#define WF2ROOTFILE_HH_

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iosfwd>

#include <TFile.h>
#include <TTree.h>
#include <TObject.h>

#include "wf2rootRecord.hh"

using namespace std;

class wf2rootFile: public TFile {

public:
	// Exception to throw when TTree creation failed
	class CreateTreeException {
	private:
		string msg;
	public:
		CreateTreeException(string errMsg) :
				msg(errMsg) {
			;
		}
		~CreateTreeException() {
			;
		}
		string GetMessage() {
			return this->msg;
		}
	};

	// Exception to throw when TBranch creation failed
	class CreateBranchException {
	private:
		string msg;
	public:
		CreateBranchException(string errMsg) :
				msg(errMsg) {
			;
		}
		~CreateBranchException() {
			;
		}
		string GetMessage() {
			return this->msg;
		}
	};

private:
	map<string, TTree*> prfTree;			// Map of the trees
	map<string, void*> prfBuffer;			// Pointers to the buffers
	wf2rootFile(const wf2rootFile& file) :	// Cannot use copy constructor
			TFile() {
		MayNotUse("wf2rootFile::wf2rootFile(const wf2rootFile& file");
	}

public:
	static UInt_t prfTreeBuffSize;		// Buffer size for the tree
	static UInt_t prfAutoSaveSize;		// Autosave size for the tree
	static string prfBranchName;		// Name of the only branch on the tree
        int EventCounter;

	wf2rootFile(const char* fname, Option_t* option = "", const char* ftitle =
			"", Int_t compress = 1) :
			TFile(fname, option, ftitle, compress) {
          EventCounter = 0;
	}

	virtual ~wf2rootFile() {				// Class Destructor
	}
	;

	virtual void Close();					// Close the file

	void CreateTree(string treeName, int nElm = 0);			// Create tree
	void FillTree(string treeName, wf2rootRecord& record);// Fill the tree with a single record

	inline TTree* GetTree(string treeName) {// Return the pointer to the tree
		if (prfTree.count(treeName) > 0)
			return prfTree[treeName];
		return 0;
	}
};

void wf2rootFile::Close() {

	// write ROOT trees
	for (map<string, TTree*>::iterator it = prfTree.begin();
			it != prfTree.end(); it++) {
		it->second->Write("", TObject::kOverwrite);
	}

//	this->Write("", TObject::kOverwrite);

	// free buffer
	for (map<string, void*>::iterator it = prfBuffer.begin();
			it != prfBuffer.end(); it++)
		if (it->second != 0)
			free(it->second);
	TFile::Close();
//	this->Close();
	return;
}

void wf2rootFile::CreateTree(string treeName, int nElm) {

	// throw exception if the tree already exists
	if (this->Get(treeName.c_str()) != 0) {
		string errMsg = "Object " + treeName + " already exists in file "
				+ this->GetName();
		cerr << errMsg << endl;
		throw wf2rootFile::CreateTreeException(errMsg);
	}

	// Create a ROOT tree with requested name
	this->cd();
	prfTree[treeName] = new TTree(treeName.c_str(), "WF2 records");
        //prfTree[treeName]->AutoSave("SaveSelf");
	prfTree[treeName]->SetAutoSave(prfAutoSaveSize);
	// throw exception if the tree cannot be created
	if (prfTree[treeName] == 0) {
		string errMsg = "Could not create the ROOT Tree ";
		cerr << errMsg << endl;
		throw wf2rootFile::CreateTreeException(errMsg);
	}

	// Allocate memory for the buffer for the tree
	unsigned neededSpace = 2 * sizeof(Long64_t) + nElm * sizeof(float);
	prfBuffer[treeName] = malloc(neededSpace);

	char leafList[50];
	sprintf(leafList, "tsec/L:tnsec/L:data[%d]/F", nElm);
	TBranch* br = prfTree[treeName]->Branch(prfBranchName.c_str(),
			prfBuffer[treeName], leafList, prfTreeBuffSize);

	// throw exception if the branch cannot be created
	if (br == 0) {
		string errMsg = "Could not create ROOT Tree Branch " + prfBranchName;
		cerr << errMsg << endl;
		throw wf2rootFile::CreateBranchException(errMsg);
	}

	return;
}

void wf2rootFile::FillTree(string treeName, wf2rootRecord& record) {

	// If the tree does not exist or the buffer area does not exist create the tree
	if (this->Get(treeName.c_str()) == 0 || prfBuffer.count(treeName) == 0) {
		this->CreateTree(treeName, record.GetData().GetSize());
	}

	record.CopyToBuffer(prfBuffer[treeName]);
	prfTree[treeName]->Fill();
        EventCounter = prfTree[treeName]->GetEntries();
        if (EventCounter%300 == 0){
          prfTree[treeName]->AutoSave("SaveSelf");
        }


	return;
}

#endif /* WF2ROOTFILE_HH_ */
