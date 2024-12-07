{
  char newmacropath[200];
  
  //get the REEPER env variable and current macropath
  const char *REEPER   = gSystem->Getenv("REEPER");
  const char *macropath = gROOT->GetMacroPath();

  //append the REEPER dir to the macropath
  sprintf(newmacropath,"%s:%s",macropath,REEPER);
  gROOT->SetMacroPath(newmacropath);
  
  //load (and recompile, if neccesary) the grimReeper library (and chanage the prompt to be more evil).
  gROOT->LoadMacro("gr.C+");
  ((TRint*)gROOT->GetApplication())->SetPrompt("reep [%d] ");
}
