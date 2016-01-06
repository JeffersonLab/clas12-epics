#!/usr/bin/env python
import math

# DO NOT USE THIS, YET


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
  <name>Display</name>
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
    <pv_name>___PVPREFIX___:pwonoff</pv_name>
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
    <name>Ellipse</name>
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

pi=4*math.atan(1)

npcal={=68
npcal

def drawCircle(xx,yy,size,pv):
    ww=circle
    ww=ww.replace('___XPOS___',str(xx))
    ww=ww.replace('___YPOS___',str(yy))
    ww=ww.replace('___SIZE___',str(size))
    ww=ww.replace('___PVPREFIX___',pv)
    print ww

def makeSector1(x0,y0,rot):

  size=10




def makeSector(xoff,yoff,angoff):

  xoffU,yoffU=0,0
  xoffV,yoffV=0,0
  xoffW,yoffW=0,0
  if angoff==30:
    yoffU += 200
    yoffV += 40
    xoffV += 180
    xoffW -= 50
    yoffW -= 40
  elif angoff!=0: sys.exit('NO')

  size=10
  xpos=0
  ypos=0
  prefix='B_DET_PCAL_HV_SEC$(SECTOR)'
  for ii in range(0,68):
    pv=prefix+'_U_E%.2d'%(ii+1)
    if ii%2==0: ypos += int(round(size/math.sqrt(2)))
    else:       ypos -= int(round(size/math.sqrt(2)))
    xposU=xpos*math.cos((angoff)*pi/180)+ypos*math.sin((angoff)*pi/180)
    yposU=ypos*math.cos((angoff)*pi/180)-xpos*math.sin((angoff)*pi/180)
    drawCircle(xposU+xoff+xoffU,yposU+yoff+yoffU,size,pv)
    if ii<62:
      pv=prefix+'_V_E%.2d'%(ii+1)
      xposV=xpos*math.cos((120+angoff)*pi/180)+ypos*math.sin((120+angoff)*pi/180)
      yposV=ypos*math.cos((120+angoff)*pi/180)-xpos*math.sin((120+angoff)*pi/180)
      if angoff==30: xposV-=10
      drawCircle(xposV+220+xoff+xoffV,yposV+410+yoff+yoffV,size,pv)
      pv=prefix+'_W_E%.2d'%(ii+1)
      xposW=xpos*math.cos((-120+angoff)*pi/180)+ypos*math.sin((-120+angoff)*pi/180)
      yposW=ypos*math.cos((-120+angoff)*pi/180)-xpos*math.sin((-120+angoff)*pi/180)
      drawCircle(xposW+480+xoff+xoffW,yposW+40+yoff+yoffW,size,pv)
    xpos += int(round(size/math.sqrt(2)))
  size=14
  xpos=size*3.8
  ypos=size*1.5
  prefix='B_DET_ECAL_HV_SEC$(SECTOR)'
  for ii in range(0,36):
    pv=prefix+'_UO_E%.2d'%(ii+1)
    if ii%2==0: ypos += int(round(size/math.sqrt(2)))
    else:       ypos -= int(round(size/math.sqrt(2)))
    xposU=xpos*math.cos((angoff)*pi/180)+ypos*math.sin((angoff)*pi/180)
    yposU=ypos*math.cos((angoff)*pi/180)-xpos*math.sin((angoff)*pi/180)
    drawCircle(xposU+5+xoff+xoffU,yposU+yoff+yoffU,size,pv)
    pv=prefix+'_VO_E%.2d'%(ii+1)
    xposV=xpos*math.cos((120+angoff)*pi/180)+ypos*math.sin((120+angoff)*pi/180)
    yposV=ypos*math.cos((120+angoff)*pi/180)-xpos*math.sin((120+angoff)*pi/180)
    drawCircle(xposV+225+xoff+xoffV,yposV+410+yoff+yoffV,size,pv)
    pv=prefix+'_WO_E%.2d'%(ii+1)
    xposW=xpos*math.cos((-120+angoff)*pi/180)+ypos*math.sin((-120+angoff)*pi/180)
    yposW=ypos*math.cos((-120+angoff)*pi/180)-xpos*math.sin((-120+angoff)*pi/180)
    if angoff==30: xposW-=10
    drawCircle(xposW+485+xoff+xoffW,yposW+15+yoff+yoffW,size,pv)
    xpos += int(round(size/math.sqrt(2)))
  size=10
  xpos=size*11.5
  ypos=size*5.1
  prefix='B_DET_ECAL_HV_SEC$(SECTOR)'
  for ii in range(0,36):
    pv=prefix+'_UI_E%.2d'%(ii+1)
    if ii%2==0: ypos += int(round(size/math.sqrt(2)))
    else:       ypos -= int(round(size/math.sqrt(2)))
    xposU=xpos*math.cos((angoff)*pi/180)+ypos*math.sin((angoff)*pi/180)
    yposU=ypos*math.cos((angoff)*pi/180)-xpos*math.sin((angoff)*pi/180)
    drawCircle(xposU+5+xoff+xoffU,yposU+yoff+yoffU,size,pv)
    pv=prefix+'_VI_E%.2d'%(ii+1)
    xposV=xpos*math.cos((120+angoff)*pi/180)+ypos*math.sin((120+angoff)*pi/180)
    yposV=ypos*math.cos((120+angoff)*pi/180)-xpos*math.sin((120+angoff)*pi/180)
    drawCircle(xposV+230+xoff+xoffV,yposV+420+yoff+yoffV,size,pv)
    pv=prefix+'_WI_E%.2d'%(ii+1)
    xposW=xpos*math.cos((-120+angoff)*pi/180)+ypos*math.sin((-120+angoff)*pi/180)
    yposW=ypos*math.cos((-120+angoff)*pi/180)-xpos*math.sin((-120+angoff)*pi/180)
    if angoff==30: xposW-=10
    drawCircle(xposW+490+xoff+xoffW,yposW+10+yoff+yoffW,size,pv)
    xpos += int(round(size/math.sqrt(2)))



print head


makeSector1(300,300,0)
#makeSector(300,300,0)
#makeSector(50,50,30)

print tail




