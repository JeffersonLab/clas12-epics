from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import WidgetUtil


NOVICE = widget.getMacroValue('NOVICE')#int(PVUtil.getDouble(pvs[0]))

FUNCTION = widget.getMacroValue('FUNCTION')

SECTOR = widget.getMacroValue('SECTOR')
REGION = widget.getMacroValue('REGION')
SLAYER = widget.getMacroValue('SLAYER')
SFG    = widget.getMacroValue('SFG')

if not SECTOR is None: SECTOR=int(SECTOR)
if not REGION is None: REGION=int(REGION)
if not SLAYER is None: SLAYER=int(SLAYER)

PREFIX = 'B_DET_DC_HV'
NSECTORS = 6
NREGIONS = 3
SLREG = { 1:[1,2], 2:[3,4], 3:[5,6] }
W_S = ['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
W_F = ['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
W_G = ['01-32','33-112']
WSFG = {'S':W_S,'F':W_F,'G':W_G}

def generateRow(ichan,pv):
  lc = WidgetUtil.createWidgetModel('org.csstudio.opibuilder.widgets.linkingContainer')
  if NOVICE>0: lc.setPropertyValue('opi_file','/CLAS12_Share/apps/caenHvApp/caenhv_channel_novice.opi')
  else:        lc.setPropertyValue('opi_file','/CLAS12_Share/apps/caenHvApp/caenhv_channel.opi')
  #try   { lc.setPropertyValue('resize_behaviour',1) }
  #catch (err) { lc.setPropertyValue('auto_size',true) }
  #    lc.setPropertyValue('resize_behavior',2)
  lc.setPropertyValue('auto_size',True)
  lc.setPropertyValue('zoom_to_fit',False)
  lc.setPropertyValue('border_style',0)
  lc.setPropertyValue('background_color','Header_Background')
  lc.addMacro('C',str(ichan))
  lc.addMacro('P',str(pv))
  widget.addChildToBottom(lc)

ichan=0
for sec in range(1,NSECTORS+1):
  if SECTOR in range(1,NSECTORS+1) and SECTOR!=sec: continue
  for reg in range(1,NREGIONS+1):
    if REGION in range(1,NREGIONS+1) and REGION!=reg: continue
    for slay in SLREG[reg]:
      if SLAYER in [1,2,3,4,5,6] and SLAYER!=slay: continue
      for sfg in ['S','F','G']:
        if SFG in ['S','F','G'] and SFG!=sfg: continue
        for wrange in WSFG[sfg]:
          pv='%s_SEC%d_R%d_SL%d_%s%s'%(PREFIX,sec,reg,slay,sfg,wrange)
          print pv
          if   FUNCTION=='ON':  PVUtil.writePV(pv+':pwonoff',1)
          elif FUNCTION=='OFF': PVUtil.writePV(pv+':pwonoff',0)
          elif FUNCTION=='LIST': generateRow(ichan,pv)
          ichan+=1


