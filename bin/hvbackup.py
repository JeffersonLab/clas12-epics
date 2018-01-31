#!/usr/bin/env python
import pygtk,gtk
import sys,time,os,commands
import getpass,grp,pwd
import subprocess,re
import epics

def exit(text,parent):
  mess = gtk.MessageDialog(parent=parent,buttons=gtk.BUTTONS_OK)
  mess.set_markup(text)
  #mess.set_position(gtk.WIN_POS_CENTER_ON_PARENT)
  mess.run()
  #mess.move(parent.get_position())
  mess.destroy()
  #sys.exit(text)

DETSHV=['CTOF_HV','FTOF_HV','ECAL_HV','PCAL_HV','FTC_HV','LTCC_HV','HTCC_HV','DC_HV','FTH_HV','FTT_HV','CND_HV','RICH_HV','MVT_HV','RICH_LV','MVT_LV']
DETSLV=['CTOF_LV','FTC_LV','HTCC_LV','DC_LV']
DETSVT=['SVT']
MISC=['BUFFERDEWAR']
DETS=DETSHV+DETSLV+DETSVT+MISC

FIELDS_HV_BURT=[':vset',':vmax',':iset',':trip',':rup',':rdn']

# key,value = field,deadband
FIELDS_HV_MYA={':pwonoff':0,':stat':0,':comms':0,':vsetrbk':0,':isetrbk':0,':vmon':0.1,':imon':1.0}
FIELDS_LV_MYA={':vsetrbk':0,':isetrbk':0,':pwrbk':0,':comms':0,':vmon':0.01,':imon':0.05}

DATADIR='/usr/clas12/DATA/burt'

SCRIPTPATH=os.path.dirname(os.path.realpath(__file__))
RELEASEPATH=re.search('(^.*/release/\d[\.\d]+)',SCRIPTPATH)
if RELEASEPATH==None: exit('Cannot Find hvbackup.py Path',None)
RELEASEPATH=RELEASEPATH.group(1)
REQDIR=RELEASEPATH+'/epics/tools/burtreq'
if not os.path.exists(REQDIR): exit('Missing REQDIR:  '+REQDIR,None)

def getChannels(det,sector=None):
  # THIS IS ONLY USED TO GENERATE THE REQ FILES
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
            #prefixes.append('B_DET_FTOF_HV_SEC%d_PANEL%s_%s_%.2d'%(ss,pp,lr,ii+1))
            prefixes.append('B_DET_FTOF_HV_SEC%d_PANEL%s_%s_E%.2d'%(ss,pp,lr,ii+1))
  elif det=='ECAL_HV':
    for ss in sectors:
      for uvw in ['U','V','W']:
        for io in ['I','O']:
          for ii in range(36):
            #prefixes.append('B_DET_ECAL_HV_SEC%d_%s%s_%.2d'%(ss,uvw,io,ii+1))
            prefixes.append('B_DET_ECAL_HV_SEC%d_%s%s_E%.2d'%(ss,uvw,io,ii+1))
  elif det=='PCAL_HV':
    nn={'U':68,'V':62,'W':62}
    for ss in sectors:
      for uvw in ['U','V','W']:
        for ii in range(nn[uvw]):
          #prefixes.append('B_DET_PCAL_HV_SEC%d_%s_%.2d'%(ss,uvw,ii+1))
          prefixes.append('B_DET_PCAL_HV_SEC%d_%s_E%.2d'%(ss,uvw,ii+1))
  elif det=='FTC_HV':
    for qq in range(4):
      for gg in range(9):
        prefixes.append('B_DET_FTC_HV_Q%dG%d'%(qq+1,gg+1))
  elif det=='FTH_HV':
    for ii in range(30):
      prefixes.append('B_DET_FTH_HV_H%.2d'%(ii+1))
  elif det=='FTT_HV':
    for ii in range(2):
      for side in ['TOP','BOT']:
        for lay in ['STR','DR']:
          prefixes.append('B_DET_FTT_HV_%.1d_%s%s'%(ii+1,side,lay))
  elif det=='LTCC_HV':
    for ss in sectors:
      for lr in ['L','R']:
        for ii in range(18):
          #prefixes.append('B_DET_LTCC_HV_SEC%d_%s_%.2d'%(ss,lr,ii+1))
          prefixes.append('B_DET_LTCC_HV_SEC%d_%s_E%.2d'%(ss,lr,ii+1))
  elif det=='HTCC_HV':
    for ss in sectors:
      for lr in ['L','R']:
        for ii in range(4):
          #prefixes.append('B_DET_HTCC_HV_SEC%d_%s_%.2d'%(ss,lr,ii+1))
          prefixes.append('B_DET_HTCC_HV_SEC%d_%s%.1d'%(ss,lr,ii+1))
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
  elif det=='DC_LV':
    for ss in sectors:
      for rr in [1,2,3]:
        prefixes.append('B_DET_DC_LV_SEC%d_R%d'%(ss,rr))
  elif det=='MVT_HV':
    for ll in [1,2,3,4,5,6]:
      prefixes.append('B_DET_FMT_HV_IN_L%d_STRIP'%(ll))
      prefixes.append('B_DET_FMT_HV_OUT_L%d_STRIP'%(ll))
      prefixes.append('B_DET_FMT_HV_L%d_DRIFT'%(ll))
    for ss in [1,2,3]:
      for ll in [1,2,3,4,5,6]:
        prefixes.append('B_DET_BMT_HV_SEC%d_L%d_DRIFT'%(ss,ll))
        prefixes.append('B_DET_BMT_HV_SEC%d_L%d_STRIP'%(ss,ll))
  elif det=='CND_HV':
    for imo in ['Inner','Middle','Outer']:
      for seg in range(1,25):
        for ch in [1,2]:
          prefixes.append('B_DET_CND_HV_%s_Seg%.2d_E%d'%(imo,seg,ch))
  elif det=='MVT_LV':
    sys.exit('NOT READY FOR MVT_LV')
  elif det=='RICH_HV':
    for tile in range(138):
      prefixes.append('B_DET_RICH_HV_TILE%.3d'%(tile+1))
  elif det=='RICH_LV':
    sys.exit('NOT READY FOR RICH_LV')

  return prefixes

def printPVsBurt(det,sector=None):
  for channel in getChannels(det,sector):
    for field in FIELDS_HV_BURT:
      print channel+field

def printPVsMya(det,sector=None):
  for channel in getChannels(det,sector):
    if channel.find('_LV_')>0:
      fieldMap=FIELDS_LV_MYA
    elif channel.find('_HV_')>0:
      fieldMap=FIELDS_HV_MYA
    else:
      print 'UNKOWN HV/LV TYPE:  ',channel
      sys.exit()
#    for field in FIELDS_HV_MYA.keys():
#      deadband=FIELDS_HV_MYA[field]
    for field in fieldMap.keys():
      deadband=fieldMap[field]
      if field==':imon':
        if   det=='FTC_HV': deadband=0.1
        elif det=='DC_HV':  deadband=0.1
      print channel+field,deadband

def printPVsAlarm(det):
  pvxml='''
      <pv name="___PV___">
        <description>___DESC___</description>
        <latching>true</latching>
        <annunciating>true</annunciating>
        <delay>10.0</delay>
        <count>0</count>
        <guidance>
          <title>Guidance</title>
          <details>Try to reset the voltage channel using the GUI. If problem persists, contact the expert.</details>
        </guidance>
        <display>
          <title>Open HV GUI</title>
          <details>/CLAS12_Share/apps/clasTreeApp/HVMonitor.opi "TYPE=4527,P=___PREFIX___,E=___PV___"</details>
        </display>
      </pv>'''
  detname=det.split('_')[0]
  system=det.split('_')[1]
  print '  <component name="'+detname+'">'
  print '    <component name="'+system+'">'
  for channel in getChannels(det):
    xx=pvxml.replace('___DESC___',detname + ' ' + system)
    xx=xx.replace('___PV___',channel)
    xx=xx.replace('___PREFIX___','B_DET_'+detname+'_'+system)
    print xx
  print '    </component>'
  print '  </component>'

def saveBurt(snpFilename,det,sector=None):
  reqFilename=REQDIR+'/'+det+'.req'
  if not os.path.exists(reqFilename): exit('Missing burt REQ file:  '+reqFilename,None)
  cmd=['burtrb','-f',reqFilename,'-o',snpFilename]
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out, err = p.communicate()
  return [out,err]

def restoreBurt(snpFilename):
  cmd=['burtwb','-f',snpFilename]
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out, err = p.communicate()
  return [out,err]

class SaveRestore:

  mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
  entry = gtk.Entry(max=0)
  progressBar = None
  filename = None
  oldChooser = None
  newChooser = None

  def chooseOldBackup(self,det):
    self.oldChooser = gtk.FileChooserDialog(
      title='RESTORE HV BACKUP',
      parent=None,
      action=gtk.FILE_CHOOSER_ACTION_OPEN,
      buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
               gtk.STOCK_OPEN,  gtk.RESPONSE_OK)
      )
    self.oldChooser.set_preview_widget_active(True)
    self.oldChooser.set_default_size(800,300)
    self.oldChooser.set_default_response(gtk.RESPONSE_CANCEL)
    self.oldChooser.set_current_folder(DATADIR+'/'+det)
    self.filename = None
    response = self.oldChooser.run()
    if response == gtk.RESPONSE_OK: self.filename = self.oldChooser.get_filename()
    self.oldChooser.destroy()
    if self.filename==None: exit('RESTORE CANCELLED.',None)
    if not os.path.exists(self.filename): exit('FILE D.N.E.\n\nRESTORE CANCELLED.',None)
    return self.filename

  def chooseNewBackup(self,det,sec):
    newChooser = gtk.Window(gtk.WINDOW_TOPLEVEL)
    newChooser.set_default_size(400,100)
    newChooser.set_title('CREATE HV BACKUP')
    box = gtk.VBox(False, 0)
    newChooser.add(box)
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
    button.connect('clicked',self.readEntry,newChooser)
    box.pack_start(button,True,True,0)
    button.show()
    self.progressBar=gtk.ProgressBar(adjustment=None)
    self.progressBar.show()
    box.pack_start(self.progressBar)
    self.filename = None
    newChooser.show()
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
    print out,err
    exit('BACKEDUP SETTINGS TO:\n\n'+snpFilename,self.newChooser)

  def restoreBurt(self,snpFilename):
    [out,err]=restoreBurt(snpFilename)
    exit('RESTORED SETTINGS FROM\n\n'+snpFilename,None)

#def getParent():
#  os.getppid()
#  with open('/proc/'+os.getppid()+'/comm') as file: lines=file.readlines()

def main():

  scriptName=sys.argv.pop(0)
  usage=scriptName+' [-b] [-m] det=detectorName save|restore'

  det=None
  filename=None
  sector=None
  saverestore=None
  printMya=False
  printBurt=False
  printAlarm=False

  for arg in sys.argv[:]:
    if arg=='-h' or arg=='--help':
      sys.exit(usage)
    elif arg=='-m':
      printMya=True
      sys.argv.remove(arg)
    elif arg=='-b':
      printBurt=True
      sys.argv.remove(arg)
    elif arg=='-a':
      printAlarm=True
      sys.argv.remove(arg)
    elif arg.find('=')>=0:
      (key,val)=arg.split('=',1)
      if   key=='det': det=val
#      elif key=='sec': sector=val
      else: sys.exit(usage)
      sys.argv.remove(arg)

#  if sector != None: sector=sector.replace('S','')
  if (det==None): sys.exit(usage)
  if (det not in DETS): sys.exit(usage)

  if printBurt:
    printPVsBurt(det)
    sys.exit()
  if printMya:
    printPVsMya(det)
    sys.exit()
  if printAlarm:
    printPVsAlarm(det)
    sys.exit()

  if len(sys.argv)!=1: sys.exit(usage)

  saverestore=sys.argv.pop()

  if saverestore!='save' and saverestore!='restore': sys.exit(usage)

  #user = pwd.getpwuid(os.getuid())[0]
  #if os.getgid() != grp.getgrnam('onliners').gr_gid:
  #    sys.exit('BACKUPS REQUIRE MEMBERSHIP IN GROUP onliners.\n\n'+user+' IS NOT A MEMBER.\n\nEXITING.')

  backup = SaveRestore()

  if saverestore=='save':
    if filename==None:
      filename = backup.chooseNewBackup(det,sector)
    backup.saveBurt(filename,det,sector)
  elif saverestore=='restore':
    if filename==None:
      filename = backup.chooseOldBackup(det)
    if filename != None: backup.restoreBurt(filename)


if __name__ == '__main__': main()
