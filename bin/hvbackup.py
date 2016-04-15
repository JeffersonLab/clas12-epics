#!/usr/bin/env python
import pygtk,gtk
import sys,time,os,commands
import getpass,grp,pwd
import subprocess,re
import epics

def exit(text):
  mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
  mess.set_markup(text)
  mess.run()
  mess.destroy()
  sys.exit(text)

DETSHV=['CTOF_HV','FTOF_HV','ECAL_HV','PCAL_HV','FTC_HV','LTCC_HV','HTCC_HV','DC_HV']
DETSLV=['CTOF_LV','FTC_LV','HTCC_LV','DC_LV']
DETS=DETSHV+DETSLV
FIELDSHV=[':vset',':vmax',':iset',':trip',':rup',':rdn']
DATADIR='/usr/clas12/DATA/burt'

SCRIPTPATH=os.path.dirname(os.path.realpath(__file__))
RELEASEPATH=re.search('(^.*/release/\d[\.\d]+)',SCRIPTPATH)
if RELEASEPATH==None: exit('Cannot Find hvbackup.py Path')
RELEASEPATH=RELEASEPATH.group(1)
REQDIR=RELEASEPATH+'/epics/apps/scripts/hvburt/req'
if not os.path.exists(REQDIR): exit('Missing REQDIR:  '+REQDIR)

def getChannels(det,sector=None):
  prefixes=[]
  sectors=[]
  for ss in range(1,7):
    if sector not in [1,2,3,4,5,6] or ss==sector:
      sectors.append(ss)
  if det=='CTOF_HV':
    for ud in ['U','D']:
      for ii in range(48):
        prefixes.append('B_DET_CTOF_HV_'+ud+'%.2d'%(ii+1))
  elif det=='FTOF_HV':
    nn={'1A':23,'1B':62,'2':5}
    for ss in sectors:
      for pp in ['1A','1B','2']:
        for lr in ['L','R']:
          for ii in range(nn[pp]):
            prefixes.append('B_DET_FTOF_HV_SEC%d_PANEL%s_%s_E%.2d'%(ss,pp,lr,ii+1))
  elif det=='ECAL_HV':
    for ss in sectors:
      for uvw in ['U','V','W']:
        for io in ['I','O']:
          for ii in range(36):
            prefixes.append('B_DET_ECAL_HV_SEC%d_%s%s_E%.2d'%(ss,uvw,io,ii+1))
  elif det=='PCAL_HV':
    nn={'U':68,'V':62,'W':62}
    for ss in sectors:
      for uvw in ['U','V','W']:
        for ii in range(nn[uvw]):
          prefixes.append('B_DET_PCAL_HV_SEC%d_%s_E%.2d'%(ss,uvw,ii+1))
  elif det=='FTC_HV':
    for qq in range(4):
      for gg in range(9):
        prefixes.append('B_DET_FTC_HV_Q%dG%d'%(qq+1,gg+1))
  elif det=='LTCC_HV':
    for ss in sectors:
      for lr in ['L','R']:
        for ii in range(18):
          prefixes.append('B_DET_LTCC_HV_SEC%d_%s_E%.2d'%(ss,lr,ii+1))
  elif det=='HTCC_HV':
    for ss in sectors:
      for lr in ['L','R']:
        for ii in range(4):
          prefixes.append('B_DET_HTCC_HV_SEC%d_%s_E%.2d'%(ss,lr,ii+1))
  elif det=='DC_HV':
    SLAYERS={1:[1,2],2:[3,4],3:[5,6]}
    SFWIRES=['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
    GWIRES= ['01-32','33-112']
    WIRES={'S':SFWIRES,'F':SFWIRES,'G':GWIRES}
    for ss in sectors:
      for rr in range(1,4):
        for ll in SLAYERS[rr]:
          for gg in ['S','F','G']:
            for ww in WIRES[gg]:
              prefixes.append('B_DET_DC_HV_SEC%d_R%d_SL%d_%s%s'%(ss,rr,ll,gg,ww))

  return prefixes

def printPVs(det,sector=None):
  for channel in getChannels(det,sector):
    for field in FIELDSHV:
      print channel+field

def saveBurt(snpFilename,det,sector=None):
  reqFilename=REQDIR+'/'+det+'.req'
  if not os.path.exists(reqFilename): exit('Missing burt REQ file:  '+reqFilename)
  burtopts='-f '+reqFilename+' -o '+snpFilename
  p = subprocess.Popen(['burtrb', burtopts], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out, err = p.communicate()
  return [out,err]

def restoreBurt(snpFilename):
  burtopts='-f '+snpFilename
  p = subprocess.Popen(['burtwb', burtopts], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out, err = p.communicate()
  return [out,err]

class SaveRestore:

  mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
  entry = gtk.Entry(max=0)
  progressBar = None
  filename = None

  def chooseOldBackup(self,det):
    chooser = gtk.FileChooserDialog(
      title='RESTORE HV BACKUP',
      parent=None,
      action=gtk.FILE_CHOOSER_ACTION_OPEN,
      buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
               gtk.STOCK_OPEN,  gtk.RESPONSE_OK)
      )
    chooser.set_preview_widget_active(True)
    chooser.set_default_size(800,300)
    chooser.set_default_response(gtk.RESPONSE_CANCEL)
    chooser.set_current_folder(DATADIR+'/'+det)
    self.filename = None
    response = chooser.run()
    if response == gtk.RESPONSE_OK: self.filename = chooser.get_filename()
    chooser.destroy()
    if self.filename==None: exit('RESTORE CANCELLED.')
    if not os.path.exists(self.filename): exit('FILE D.N.E.\n\nRESTORE CANCELLED.')
    return self.filename

  def chooseNewBackup(self,det,sec):
    win = gtk.Window(gtk.WINDOW_TOPLEVEL)
    win.set_default_size(400,100)
    win.set_title('CREATE HV BACKUP')
    box = gtk.VBox(False, 0)
    win.add(box)
    box.show()
    text = gtk.Label()
    text2 = gtk.Label()
    text.show()
    text2.show()
    text2.set_markup('\nENTER FILENAME:\n')
    box.pack_start(text2)
    text.set_markup(DATADIR+'/'+det+'\n')
    box.pack_start(text)
    basename = time.strftime(det+'-%Y_%m_%d-%H_%M_%S.snp')
    self.entry.set_text(basename)
    box.pack_start(self.entry,True,True,0)
    self.entry.show()
    button = gtk.Button(stock=gtk.STOCK_OK)
    button.connect('clicked',self.readEntry,win)
    box.pack_start(button,True,True,0)
    button.show()
    self.progressBar=gtk.ProgressBar(adjustment=None)
    self.progressBar.show()
    box.pack_start(self.progressBar)
    self.filename = None
    win.show()
    gtk.main()
#        win.destroy()
    return DATADIR+'/'+det+'/'+self.filename

  def readEntry(self,widget,win):
    tmp = DATADIR+'/'+self.entry.get_text()
    if os.path.exists(tmp):
      mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
      mess.set_markup('FILE ALREADY EXISTS, TRY AGAIN.')
      mess.run()
      mess.destroy()
      return
    self.filename = self.entry.get_text()
    gtk.main_quit()

  def saveBurt(self,snpFilename,det,sector):
    [out,err]=saveBurt(snpFilename,det,sector)
    exit('BACKEDUP SETTINGS TO:\n\n'+snpFilename)

  def restoreBurt(self,snpFilename):
    [out,err]=restoreBurt(snpFilename)
    exit('RESTORED SETTINGS FROM\n\n'+snpFilename)

def main():

  scriptName=sys.argv.pop(0)
  usage=scriptName+' [sec=S#] det=detectorName save/restore'

  det=None
  sector=None
  saverestore=None
  printOnly=False

  for arg in sys.argv[:]:
    if arg=='-h' or arg=='--help':
      sys.exit(usage)
    elif arg=='-p':
      printOnly=True
      sys.argv.remove(arg)
    elif arg.find('=')>=0:
      (key,val)=arg.split('=',1)
      if   key=='det': det=val
      elif key=='sec': sector=val
      else: sys.exit(usage)
      sys.argv.remove(arg)

  if sector != None: sector=sector.replace('S','')
  if (det==None): sys.exit(usage)
  if (det not in DETS): sys.exit(usage)

  if printOnly:
    printPVs(det)
    sys.exit()

  if len(sys.argv)!=1: sys.exit(usage)

  saverestore=sys.argv.pop()

  if saverestore!='save' and saverestore!='restore': sys.exit(usage)

  user = pwd.getpwuid(os.getuid())[0]
  if os.getgid() != grp.getgrnam('onliners').gr_gid:
      exit('BACKUPS REQUIRE MEMBERSHIP IN GROUP onliners.\n\n'+user+' IS NOT A MEMBER.\n\nEXITING.')

  backup = SaveRestore()

  if saverestore=='save':
    filename = backup.chooseNewBackup(det,sector)
    backup.saveBurt(filename,det,sector)
  elif saverestore=='restore':
    filename = backup.chooseOldBackup(det)
    if filename != None: backup.restoreBurt(filename)


if __name__ == '__main__': main()
