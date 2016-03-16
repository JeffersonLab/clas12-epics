#!/usr/bin/env python
import math,sys

PREFIX='B_DET_LTCC_HV'

HEAD='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <TYPE>4527</TYPE>
    <DET>LTCC</DET>
  </macros>
  <wuid>6ed2d5b9:150f8592e9f:-7fc7</wuid>
  <boy_version>3.2.16.20140409</boy_version>
  <scripts />
  <show_ruler>true</show_ruler>
  <height>1000</height>
  <name></name>
  <snap_to_geometry>true</snap_to_geometry>
  <show_grid>false</show_grid>
  <background_color>
    <color name="Header_Background" red="77" green="77" blue="77" />
  </background_color>
  <foreground_color>
    <color red="192" green="192" blue="192" />
  </foreground_color>
  <widget_type>Display</widget_type>
  <show_close_button>true</show_close_button>
  <width>1000</width>
  <rules />
  <show_edit_range>true</show_edit_range>
  <grid_space>1</grid_space>
  <auto_scale_widgets>
    <auto_scale_widgets>false</auto_scale_widgets>
    <min_width>-1</min_width>
    <min_height>-1</min_height>
  </auto_scale_widgets>
  <y>0</y>
  <x>0</x>
'''

TAIL='''
</display>
'''

WIDGHEAD='''
  <widget typeId="org.csstudio.opibuilder.widgets.polygon" version="1.0.0">
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <visible>true</visible>
    <fill_level>0.0</fill_level>
    <line_color>
      <color red="128" green="0" blue="255" />
    </line_color>
    <wuid>6ed2d5b9:150f8592e9f:-7e38</wuid>
    <rotation_angle>0.0</rotation_angle>
    <anti_alias>true</anti_alias>
    <name>Polygon</name>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <alpha>255</alpha>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <points>
'''
WIDGPT='''    <point x="^^^XPOS^^^" y="^^^YPOS^^^" />'''
WIDGTAIL='''
    </points>

    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^</P>
        </macros>
        <replace>2</replace>
        <description>Open Controls</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^:pwonoff</pv_name>
        <value>1</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn On</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^:pwonoff</pv_name>
        <value>0</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn Off</description>
      </action>
    </actions>

    <scripts>
      <path pathString="../../apps/caenHvApp/set_status_led2.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^.L</pv>
        <pv trig="true">^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^.T</pv>
      </path>
    </scripts>
    <transparent>false</transparent>
    <pv_name>^^^PREFIX^^^_SEC^^^SECTOR^^^_^^^LEFTRIGHT^^^_E^^^CHANNEL^^^</pv_name>
    <background_color>
      <color name="Off" red="60" green="100" blue="60" />
    </background_color>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <widget_type>Polygon</widget_type>
    <enabled>true</enabled>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
    <height>^^^HEIGHT^^^</height>
    <width>^^^WIDTH^^^</width>
    <line_style>0</line_style>
    <border_style>0</border_style>
    <rules />
    <pv_value />
    <border_width>1</border_width>
    <line_width>0</line_width>
    <horizontal_fill>true</horizontal_fill>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <y>^^^YPOS^^^</y>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <x>^^^XPOS^^^</x>
  </widget>
'''

D2R=4*math.atan(1)/180
globoff=[400,500]
off=0.1
scale=20
slope = 0.57735

def transformPoint(pt,xoff,yoff,angle):
  xx,yy=pt[0],pt[1]
  pt[0]=xx*math.cos(angle*D2R)+yy*math.sin(angle*D2R)
  pt[1]=yy*math.cos(angle*D2R)-xx*math.sin(angle*D2R)
  pt[0]+=xoff
  pt[1]+=yoff
  return  pt


def genSector(sector,xoff,yoff,angle):

  for channel in range(18):

    points = [ [-1*channel-off,    0-off],
               [-1*(channel+1)+off,0-off],
               [-1*(channel+1)+off,-slope*(3+channel)+off],
               [-1*channel-off,    -slope*(2+channel)+off-0.12] ]

    for leftright in ['R','L']:

      print WIDGHEAD

      ymin,xmin=99999,99999
      ymax,xmax=-99999,-99999

      for point in points:

        xx=scale*point[0]
        yy=scale*point[1]

        if leftright=='L':
          yy=-yy

        point=[xx,yy]
        [xx,yy]=transformPoint(point,xoff,yoff,angle)

        pt=WIDGPT
        pt=pt.replace('^^^XPOS^^^','%d'%(int(round(xx))))
        pt=pt.replace('^^^YPOS^^^','%d'%(int(round(yy))))
        if xx>xmax: xmax=xx
        if xx<xmin: xmin=xx
        if yy>ymax: ymax=yy
        if yy<ymin: ymin=yy
        print pt,

      height=ymax-ymin
      width=xmax-xmin
      asdf=WIDGTAIL
      asdf=asdf.replace('^^^HEIGHT^^^','%d'%(int(round(height))))
      asdf=asdf.replace('^^^WIDTH^^^','%d'%(int(round(width))))
      asdf=asdf.replace('^^^XPOS^^^','%d'%(int(round(globoff[0]+xmin))))
      asdf=asdf.replace('^^^YPOS^^^','%d'%(int(round(globoff[1]+ymin))))
      asdf=asdf.replace('^^^CHANNEL^^^','%.2d'%(channel+1))
      asdf=asdf.replace('^^^SECTOR^^^','%d'%(sector))
      asdf=asdf.replace('^^^PREFIX^^^',PREFIX)
      asdf=asdf.replace('^^^LEFTRIGHT^^^',leftright)
      print asdf


print HEAD
genSector(1,0,0,0)
genSector(2,35,-60,-60)
genSector(3,100,-60,-120)
genSector(4,135,0,-180)
genSector(5,100,60,120)
genSector(6,35,60,60)
print TAIL

