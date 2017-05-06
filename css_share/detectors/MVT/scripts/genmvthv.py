#!/usr/bin/env python
import math,sys

HEAD='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <show_close_button>true</show_close_button>
  <rules />
  <wuid>2da4dada:138bb0b2666:-7ff6</wuid>
  <show_grid>false</show_grid>
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <scripts />
  <height>600</height>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <TYPE>1527</TYPE>
    <DET>MVT</DET>
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
  <width>500</width>
  <x>-1</x>
  <name>Display</name>
  <grid_space>1</grid_space>
  <show_ruler>true</show_ruler>
  <y>-1</y>
  <snap_to_geometry>true</snap_to_geometry>
  <foreground_color>
    <color name="GRID" red="90" green="90" blue="90" />
  </foreground_color>
  <actions hook="false" hook_all="false" />
'''

TAIL='''
</display>
'''

WIDG='''
<widget typeId="org.csstudio.opibuilder.widgets.polygon" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <line_width>0</line_width>
    <horizontal_fill>true</horizontal_fill>
    <alarm_pulsing>false</alarm_pulsing>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-5d836a5:15bddc23b5a:-7ace</wuid>
    <transparent>false</transparent>
    <points>
    ---POINTS---
    </points>
    <pv_value />
    <alpha>255</alpha>
    <rotation_angle>0.0</rotation_angle>
    <scripts>
      <path pathString="../../apps/caenHvApp/set_status_led2.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">$(pv_name):stat</pv>
        <pv trig="true">$(pv_name):comms</pv>
      </path>
    </scripts>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <height>---HEIGHT---</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>---PV---</pv_name>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <anti_alias>true</anti_alias>
    <line_style>0</line_style>
    <widget_type>Polygon</widget_type>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="30" green="144" blue="255" />
    </background_color>
    <width>---WIDTH---</width>
    <x>---X---</x>
    <name>---WIDGNAME---</name>
    <y>---Y---</y>
    <fill_level>0.0</fill_level>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(pv_name)</P>
        </macros>
        <replace>0</replace>
        <description>Open Controls</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>$(pv_name):pwonoff</pv_name>
        <value>1</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn On</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>$(pv_name):pwonoff</pv_name>
        <value>0</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn Off</description>
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

def getPoints(npoints,radius,center,thetaRange):
  d2r=3.141592/180
  pts=[]
  for ii in range(npoints+1):
    theta=thetaRange[0]+ii*(thetaRange[1]-thetaRange[0])/npoints
    xx=center[0]+radius[0]*math.cos(theta*d2r)
    yy=center[1]+radius[0]*math.sin(theta*d2r)
    pts.append([int(round(xx)),int(round(yy))])
  for ii in range(npoints+1):
    theta=thetaRange[1]+ii*(thetaRange[0]-thetaRange[1])/npoints
    xx=center[0]+radius[1]*math.cos(theta*d2r)
    yy=center[1]+radius[1]*math.sin(theta*d2r)
    pts.append([int(round(xx)),int(round(yy))])
  return pts

def getLimits(points):
  xmin,ymin= 9999999, 9999999
  xmax,ymax=-9999999,-9999999
  for pt in points:
    if pt[0]<xmin: xmin=pt[0]
    if pt[1]<ymin: ymin=pt[1]
    if pt[0]>xmax: xmax=pt[0]
    if pt[1]>ymax: ymax=pt[1]
  return {'xmin':xmin,'xmax':xmax,'ymin':ymin,'ymax':ymax}

def getWidth(points):
  limits=getLimits(points)
  return limits['xmax']-limits['xmin']

def getHeight(points):
  limits=getLimits(points)
  return limits['ymax']-limits['ymin']

def getX(points): return getLimits(points)['xmin']
def getY(points): return getLimits(points)['ymin']

def getPointsXML(points):
  ptstr=''
  for pt in points:
    ptstr+='<point x="%d" y="%d" />\n'%(pt[0],pt[1])
  return ptstr

def getWidget(specs):
  ww=WIDG
  ww=ww.replace('---PV---',specs['pv'])
  ww=ww.replace('---WIDGNAME---',specs['pv'])
  ww=ww.replace('---POINTS---',getPointsXML(specs['points']))
  ww=ww.replace('---HEIGHT---',str(getHeight(specs['points'])))
  ww=ww.replace('---WIDTH---',str(getWidth(specs['points'])))
  ww=ww.replace('---X---',str(getX(specs['points'])))
  ww=ww.replace('---Y---',str(getY(specs['points'])))
  return ww

def getSector(prefix,npts,offset,angleRange):
  widgets,roff=[],0
  for ch in range(12):
    pv='%s%.2d'%(prefix,ch)
    radiiRange=[30+ch*11+roff,30+ch*11+9+roff]
    #radiiRange=[50+ch*15+roff,50+ch*15+12+roff]
    points=getPoints(npts,radiiRange,offset,angleRange)
    widgets.append(getWidget({'pv':pv,'points':points}))
    if ch%2==1: roff+=2
  return widgets


NPTS=13
OFFSET=[260,260]

WIDGETS=[]
WIDGETS.append(getSector('B_HW_MVTHV_Sl06_Ch',NPTS,OFFSET,[31,149]))
WIDGETS.append(getSector('B_HW_MVTHV_Sl08_Ch',NPTS,OFFSET,[151,269]))
WIDGETS.append(getSector('B_HW_MVTHV_Sl10_Ch',NPTS,OFFSET,[271,389]))

print HEAD
print WIDGETS
print TAIL


