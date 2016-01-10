#!/usr/bin/env python
import pygtk,gtk
import sys,time,os,commands
import getpass,grp,pwd
import epics

FIELDS=[':vset',':iset',':trip',':rup',':rdn','.NAME']

DATADIR='/usr/clas12/DATA/hvbackup'

def exit(text):
  mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
  mess.set_markup(text)
  mess.run()
  mess.destroy()
  sys.exit(text)

def getChannels(det,sector):
  prefixes=[]
  sectors=[]
  for ss in range(1,7):
    if sector==None or ss==sector:
      sectors.append(ss)
  if det=='CTOF':
    for ud in ['U','D']:
      for ii in range(48):
        prefixes.append('B_DET_CTOF_HV_'+ud+'%.2d'%(ii+1))
  elif det=='FTOF':
    nn={'1A':23,'1B':62,'2':5}
    for ss in sectors:
      for pp in ['1A','1B','2']:
        for lr in ['L','R']:
          for ii in range(nn[pp]):
            prefixes.append('B_DET_FTOF_HV_SEC%d_PANEL%s_%s_E%.2d'%(ss,pp,lr,ii+1))
  elif det=='ECAL':
    for ss in sectors:
      for uvw in ['U','V','W']:
        for io in ['I','O']:
          for ii in range(36):
            prefixes.append('B_DET_ECAL_HV_SEC%d_%s%s_E%.2d'%(ss,uvw,io,ii+1))
  elif det=='PCAL':
    nn={'U':68,'V':62,'W':62}
    for ss in sectors:
      for uvw in ['U','V','W']:
        for ii in range(nn[uvw]):
          prefixes.append('B_DET_PCAL_HV_SEC%d_%s_E%.2d'%(ss,uvw,ii+1))
  elif det=='FTC':
    for qq in range(4):
      for gg in range(9):
        prefixes.append('B_DET_FTC_HV_Q%dG%d'%(qq+1,gg+1))
  return prefixes




class SaveRestore:

  mess = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
  entry = gtk.Entry(max=0)
  progressBar = None
  filename = None

  def oldBackup(self,det):
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
    if response == gtk.RESPONSE_OK:
      self.filename = chooser.get_filename()
    chooser.destroy()
    if self.filename==None:
      exit('RESTORE CANCELLED.')
    if not os.path.exists(self.filename):
      exit('FILE D.N.E.\n\nRESTORE CANCELLED.')
    return self.filename

  def newBackup(self,det,sec):
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
    basename = time.strftime(det+'-%Y_%m_%d-%H_%M_%S.txt')
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
#    text3 = gtk.Label()
#    text3.set_markup('\n(May take a minute after clicking OK)')
#    text3.show()
#    box.pack_start(text3)
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

  def save(self,filename,det,sector):
    lines=[]
    prefixes=getChannels(det,sector)
    for prefix in prefixes:
      line = prefix+' '
      for field in FIELDS:
        pv = prefix+field
        val = epics.caget(pv)
        line += field+'='+str(val)+' '
      lines.append(line)
      frac=float(len(lines))/len(prefixes)
      self.progressBar.set_fraction(frac)
      self.progressBar.set_text('%d%%'%(round(frac*100)))
#      self.progressBar.get_fraction()
#      self.progressBar.pulse()
      gtk.main_iteration()
      #print line

    file=open(filename,'w')
    for xx in lines: print >> file, xx
    file.close()
    os.chmod(filename,0444) # set it unwriteable
    exit('BACKEDUP VOLTAGES TO:\n\n'+filename)

  def restore(self,filename):
    return
    caputs=[]
    lines=open(filename,'r').readlines()
    for line in lines:
      cols = line.rstrip().split()
      prefix=cols.pop(0)
      for col in cols:
        keyval=col.split('=')
        if len(keyval)!=2:
          exit('INVALID FILE:\n\n'+filename+'\n\nNOT RESTORING.')
        field=keyval[0]
        if field=='.NAME': continue
        try: val = float(col[1])
        except ValueError: exit('INVALID FILE:\n\n'+filename+'\n\nNOT RESTORING.')
        pv=prefix+field
        caputs.append((pv,val))
        print pv,val
#      epics.caput(pv,val)
    exit('RESTORED '+str(len(lines))+' VOLTAGES FROM:\n\n'+filename)

def main():

  scriptName=sys.argv.pop(0)
  usage=scriptName+' [options] det=detectorName save/restore'

  det=None
  sector=None
  saverestore=None

  for arg in sys.argv:
    if arg=='-h' or arg=='--help': sys.exit(usage)

  for arg in sys.argv[:]:
    if arg.find('=')<0: continue
    (key,val)=arg.split('=',1)
    if   key=='det':    det=val
    elif key=='sector': sector=val
    else: sys.exit(usage)
    sys.argv.remove(arg)

  if (det==None): sys.exit(usage)
  if len(sys.argv)!=1: sys.exit(usage)

  saverestore=sys.argv.pop()

  if saverestore!='save' and saverestore!='restore': sys.exit(usage)

  user = pwd.getpwuid(os.getuid())[0]
  if os.getgid() != grp.getgrnam('clas-3').gr_gid:
      exit('BACKUPS REQUIRE MEMBERSHIP IN GROUP clas-3.\n\n'+user+' IS NOT A MEMBER.\n\nEXITING.')

  backup = SaveRestore()

  if saverestore=='save':
    filename = backup.newBackup(det,sector)
    backup.save(filename,det,sector)
  elif saverestore=='restore':
    filename = backup.oldBackup(det)
    if filename != None: backup.restore(filename)


if __name__ == '__main__': main()
