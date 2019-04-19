#!/usr/bin/env python
import sys,os,argparse,subprocess,getpass

if getpass.getuser() != 'clasrun':
  sys.exit('ERROR:  This requires user=clasrun, but you are '+getpass.getuser())

cli=argparse.ArgumentParser(description='CAEN HV Mainframe Reset')
cli.add_argument('--hard',help='hard reset', action='store_true', default=False)
cli.add_argument('--soft',help='soft reset', action='store_true', default=False)
cli.add_argument('mainframe',help='name of mainframe')
args=cli.parse_args()

opt=None
if args.hard and args.soft: cli.error('Must choose only one of --hard or --soft.')
elif args.hard:  opt='--hard'
elif args.soft:  opt='--soft'
else:  cli.error('ERROR:  Must choose one of --hard or --soft.')

clonParms=os.getenv('CLON_PARMS')
epics=os.getenv('EPICS')

if not os.path.isdir(clonParms):
  sys.exit('ERROR:  $CLON_PARMS does not exist: >%s<'%clonParms)

configFile=clonParms+'/tsconnect/tsconnect.conf'

if not os.path.isfile(configFile):
  sys.exit('ERROR:  tsconnect config file does not exist: >%s<'%configFile)

exe=epics+'/tools/caenhvReset/caenhvReset'
if not os.path.isfile(exe):
  sys.exit('ERROR:  cannot find file: >%s<'%exe)

device=None
with open(configFile,'r') as f:
  for line in f.readlines():
    if line.find(args.mainframe+'_reset')>=0:
      device=line.strip().split()[0]
      break

if device is None:
  sys.exit('ERROR:  Could not find device %s_reset in tsconnect config file %s'%(args.mainframe,configFile))

print subprocess.check_output(['ssh','clon00','sudo',exe,opt,'/dev/tty'+device])

