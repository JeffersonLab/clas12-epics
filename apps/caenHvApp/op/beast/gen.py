#!/usr/bin/env python

header='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<config name="HallB">
    <component name="__DETECTOR__">
        <component name="HV">'''
footer='''
        </component>
    </component>
</config>'''
sectionHeader='''
            <component name="__SECTION__">'''
sectionFooter='''
            </component>'''
pvTemplate='''
                <pv name="__PV__">
                    <description>__DESC__</description>
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
                        <details>/CLAS12_Share/apps/clasTreeApp/HVMonitor.opi &quot;TYPE=__SYTYPE__,P=__PV__,E=__PV__&quot;</details>
                    </display>
                </pv>'''

pvs=[]
for row in open('../../Db/subs/HVBAND.substitutions','r'):
  cols=row.strip().split('"')
  if len(cols) != 35: continue
  sytype,det,ele=cols[5],cols[13],cols[15]
  pv='B_DET_%s_HV_%s'%(det,ele)
  if ele.find('empty')>=0 or ele.find('spare')>=0:
    continue
  if ele[0]=='V':
    layer = 'Vetoes'
  else:
    layer = 'Layer %d'%int(ele[0])
  pvs.append({'sytype':sytype,'det':det,'section':layer,'pv':pv,'ele':ele})

sections=[]
for pv in pvs:
  if pv['section'] not in sections:
    sections.append(pv['section'])

def myReplace(line,pv):
  xx=line.replace('__DETECTOR__',pvs[0]['det'])
  xx=xx.replace('__SECTION__',pv['section'])
  xx=xx.replace('__SYTYPE__',pv['sytype'])
  xx=xx.replace('__DESC__','%s HV %s'%(pv['det'],pv['ele']))
  xx=xx.replace('__PV__',pv['pv'])
  return xx

print header.replace('__DETECTOR__',pvs[0]['det'])
for section in sections:
  print sectionHeader.replace('__SECTION__',section)
  for pv in pvs:
    if pv['section']!=section:
      continue
    for line in pvTemplate.split('\n'):
      print myReplace(line,pv)
  print sectionFooter
print footer

