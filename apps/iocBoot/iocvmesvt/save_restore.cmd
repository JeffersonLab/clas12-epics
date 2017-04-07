
# this should enable auto-remounting (e.g. if fileserver is rebooted)
# but it does not appear to work (based on manually unmounting with nfsUnmount)
#  save_restoreSet_NFSHost("clonfs1","129.57.167.16")

## General settings
  save_restoreSet_status_prefix("$(IOC):")
  save_restoreSet_Debug(0)
  save_restoreSet_IncompleteSetsOk(1)
  save_restoreSet_DatedBackupFiles(1)
  save_restoreSet_NumSeqFiles(3)
  save_restoreSet_SeqPeriodInSeconds(30)

  ## Specify paths
  set_savefile_path("/DATA/autosave/iocvmesvt")
  set_requestfile_path(".")
  set_requestfile_path("$(TOP)/req")

  set_pass0_restoreFile("info_positions.sav")
  set_pass1_restoreFile("info_settings.sav")

