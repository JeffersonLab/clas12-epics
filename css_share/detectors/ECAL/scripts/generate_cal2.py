#!/usr/bin/env python
import math

head='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <show_close_button>true</show_close_button>
  <rules />
  <wuid>2da4dada:138bb0b2666:-7ff6</wuid>
  <show_grid>false</show_grid>
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <scripts />
  <height>1000</height>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <DET>ECAL</DET>
    <TYPE>4527</TYPE>
  </macros>
  <boy_version>4.0.103.201511111440</boy_version>
  <show_edit_range>true</show_edit_range>
  <widget_type>Display</widget_type>
  <auto_scale_widgets>
    <auto_scale_widgets>false</auto_scale_widgets>
    <min_width>-1</min_width>
    <min_height>-1</min_height>
  </auto_scale_widgets>
  <background_color>
    <color name="OPI_Background" red="50" green="50" blue="50" />
  </background_color>
  <width>1000</width>
  <x>-1</x>
  <name>ECAL HV</name>
  <grid_space>6</grid_space>
  <show_ruler>true</show_ruler>
  <y>-1</y>
  <snap_to_geometry>false</snap_to_geometry>
  <foreground_color>
    <color red="192" green="192" blue="192" />
  </foreground_color>
  <actions hook="false" hook_all="false" />
'''

circle='''
  <widget typeId="org.csstudio.opibuilder.widgets.Ellipse" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <line_width>0</line_width>
    <horizontal_fill>true</horizontal_fill>
    <alarm_pulsing>false</alarm_pulsing>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-62687a87:152087533d9:18db</wuid>
    <transparent>false</transparent>
    <pv_value />
    <alpha>255</alpha>
    <bg_gradient_color>
      <color red="255" green="255" blue="255" />
    </bg_gradient_color>
    <scripts>
      <path pathString="/CLAS12_Share/apps/caenHvApp/set_status_led2.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">___PVPREFIX___:comms</pv>
        <pv trig="true">___PVPREFIX___:stat</pv>
      </path>
    </scripts>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <height>___SIZE___</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>___PVPREFIX___.NAME</pv_name>
    <gradient>false</gradient>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <anti_alias>true</anti_alias>
    <line_style>0</line_style>
    <widget_type>Ellipse</widget_type>
    <fg_gradient_color>
      <color red="255" green="255" blue="255" />
    </fg_gradient_color>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color name="Off" red="60" green="100" blue="60" />
    </background_color>
    <width>___SIZE___</width>
    <x>___XPOS___</x>
    <name>LED___PVPREFIX___</name>
    <y>___YPOS___</y>
    <fill_level>0.0</fill_level>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>___PVPREFIX___</P>
        </macros>
        <replace>2</replace>
        <description></description>
      </action>
    </actions>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
    <line_color>
      <color red="128" green="0" blue="255" />
    </line_color>
  </widget>
'''


tail='''
</display>
'''

D2R=4*math.atan(1)/180
NPCAL=68
NECAL=36

OFFP={'U':[-4.0,0.0],'V':[-1.0,5.0],'W':[ 4.0,0.0]}
OFFI={'U':[ 0.0,0.5],'V':[ 0.0,1.0],'W':[-0.2,0.0]}
OFFO={'U':[-1.0,0.0],'V':[ 0.0,2.5],'W':[ 1.0,0.0]}
OFF={'P':OFFP,'I':OFFI,'O':OFFO}

def drawCircle(pt):
  ww=circle
  ww=ww.replace('___XPOS___',str(int(round(pt['x']))))
  ww=ww.replace('___YPOS___',str(int(round(pt['y']))))
  ww=ww.replace('___SIZE___',str(pt['d']))
  ww=ww.replace('___PVPREFIX___',pt['pv'])
  print ww

def transformPoint(pt,xoff,yoff,angle):
  xx,yy=pt['x'],pt['y']
  pt['x']=xx*math.cos(angle*D2R)+yy*math.sin(angle*D2R)
  pt['y']=yy*math.cos(angle*D2R)-xx*math.sin(angle*D2R)
  pt['x']+=xoff
  pt['y']+=yoff

def makeLayer(sector,xoff,yoff,angle,diameter,pio):
  pts=[]
  x0,y0=0,0
  if pio=='P':
    prefix='B_DET_PCAL_HV_SEC'+str(sector)
    nelements=NPCAL
  else:
    prefix='B_DET_ECAL_HV_SEC'+str(sector)
    nelements=NECAL
  for ii in range(0,nelements):
    side = nelements * (diameter+1) / 2
    height = side * math.sqrt(3) / 2
    x0V,y0V = x0 + side/2 , y0 - height/2
    x0U,y0U = x0 + side/2 , y0 - height/2
    x0W,y0W = x0          , y0 + height/2
    xV = x0V - ii * (diameter+1) / 2 - diameter * 1
    if ii%2==0: yV = y0V + (diameter+1) * math.sqrt(3)/2
    else:       yV = y0V
    ptU={'x':xV,'y':yV,'d':diameter,'pv':prefix+'_U_E%.2d'%(ii+1)}
    ptV={'x':xV,'y':yV,'d':diameter,'pv':prefix+'_V_E%.2d'%(ii+1)}
    ptW={'x':xV,'y':yV,'d':diameter,'pv':prefix+'_W_E%.2d'%(ii+1)}
    transformPoint(ptU,diameter*OFF[pio]['U'][0],diameter*OFF[pio]['U'][1],-120)
    transformPoint(ptV,diameter*OFF[pio]['V'][0],diameter*OFF[pio]['V'][1],   0)
    transformPoint(ptW,diameter*OFF[pio]['W'][0],diameter*OFF[pio]['W'][1], 120)
    pts.append(ptU)
    if ii>=62: continue
    pts.extend([ptV,ptW])
  return pts

def makeSector(sector,xoff,yoff,angle):
  pts=[]
  pts.extend(makeLayer(sector,xoff,yoff,angle,10,'P'))
  pts.extend(makeLayer(sector,xoff,yoff,angle,12,'I'))
  pts.extend(makeLayer(sector,xoff,yoff,angle,10,'O'))
  for pt in pts:
    transformPoint(pt,xoff,yoff,angle)
    drawCircle(pt)

print head
makeSector(1,200,450, 90)
makeSector(2,350,200, 30)
makeSector(3,650,200,-30)
makeSector(4,800,450,-90)
makeSector(5,650,700,-150)
makeSector(6,350,700,-210)
print tail


