## General settings
save_restoreSet_status_prefix("iocscalerTest:")
save_restoreSet_Debug(0)
save_restoreSet_IncompleteSetsOk(1)
save_restoreSet_DatedBackupFiles(1)
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(30)

## Specify paths
set_savefile_path(iocdata,     "autosave/iocscalerTest")

set_requestfile_path(startup,  "")
set_requestfile_path(top,      "req")
set_requestfile_path(startup,  "autosave")
set_requestfile_path(autosave, "asApp/Db")
set_requestfile_path(calc,     "calcApp/Db")
set_requestfile_path(mca,      "mcaApp/Db")
set_requestfile_path(sscan,    "sscanApp/Db")
set_requestfile_path(std,      "stdApp/Db")

## Restore passes
set_pass0_restoreFile("info_positions.sav")
set_pass0_restoreFile("info_settings.sav")
set_pass1_restoreFile("info_settings.sav")
set_pass1_restoreFile("scaler16m_settings.sav")
set_pass1_restoreFile("sixty_hz_settings.sav")

