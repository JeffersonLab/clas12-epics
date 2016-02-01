#!/usr/bin/env python
import math

head='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <DET>B_DET_FTOF_HV</DET>
    <TYPE>4527</TYPE>
  </macros>
  <wuid>-1440ecc8:14f850aa82a:-67a8</wuid>
  <boy_version>3.2.16.20140409</boy_version>
  <scripts />
  <show_ruler>true</show_ruler>
  <height>700</height>
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
  <show_close_button>false</show_close_button>
  <width>700</width>
  <rules />
  <show_edit_range>true</show_edit_range>
  <grid_space>1</grid_space>
  <auto_scale_widgets>
    <auto_scale_widgets>false</auto_scale_widgets>
    <min_width>-1</min_width>
    <min_height>-1</min_height>
  </auto_scale_widgets>
  <actions hook="false" hook_all="false" />
  <y>-1</y>
  <x>-1</x>
'''

tail='''
</display>
'''

led='''
  <widget typeId="org.csstudio.opibuilder.widgets.linkingContainer" version="1.0.0">
    <macros>
      <include_parent_macros>true</include_parent_macros>
      <P>$(DET)_aaaCHANaaa</P>
    </macros>
    <visible>true</visible>
    <wuid>-1440ecc8:14f850aa82a:-6616</wuid>
    <auto_size>false</auto_size>
    <scripts />
    <zoom_to_fit>true</zoom_to_fit>
    <height>aaaLEDSIZEaaa</height>
    <name>Linking Container</name>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <opi_file>aaaOPIFILEaaa</opi_file>
    <foreground_color>
      <color red="192" green="192" blue="192" />
    </foreground_color>
    <background_color>
      <color name="Header_Background" red="77" green="77" blue="77" />
    </background_color>
    <group_name></group_name>
    <enabled>true</enabled>
    <widget_type>Linking Container</widget_type>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
    <width>aaaLEDSIZEaaa</width>
    <border_style>0</border_style>
    <rules />
    <border_width>1</border_width>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <y>aaaYPOSaaa</y>
    <actions hook="false" hook_all="false" />
    <x>aaaXPOSaaa</x>
    <tooltip></tooltip>
  </widget>
'''

print head

NSECTORS=6
NPANEL1A=23
NPANEL1B=5
NPANEL2=62


ypos=40
for sec in range(1,NSECTORS+1):
  for lr in ['L','R']:
    xpos=40
    for ii in range(1,NPANEL1A+1):
      dd=led
      dd=dd.replace('aaaCHANaaa','SEC%d_PANEL1A_%s_E%.2d'%(sec,lr,ii))
      dd=dd.replace('aaaXPOSaaa',str(xpos))
      dd=dd.replace('aaaYPOSaaa',str(ypos))
      dd=dd.replace('aaaLEDSIZEaaa','20')
      dd=dd.replace('aaaOPIFILEaaa','/CLAS12_Share/apps/caenHvApp/status_channel_led.opi')
      print dd
      xpos += 20
    xpos += 20
    for ii in range(1,NPANEL1B+1):
      dd=led
      dd=dd.replace('aaaCHANaaa','SEC%d_PANEL2_%s_E%.2d'%(sec,lr,ii))
      dd=dd.replace('aaaXPOSaaa',str(xpos))
      dd=dd.replace('aaaYPOSaaa',str(ypos))
      dd=dd.replace('aaaLEDSIZEaaa','20')
      dd=dd.replace('aaaOPIFILEaaa','/CLAS12_Share/apps/caenHvApp/status_channel_led.opi')
      print dd
      xpos += 20
    ypos += 20
  ypos += 10

ypos += 20
for sec in range(1,NSECTORS+1):
  for lr in ['L','R']:
    xpos=40
    for ii in range(1,NPANEL2+1):
      dd=led
      dd=dd.replace('aaaCHANaaa','SEC%d_PANEL1B_%s_E%.2d'%(sec,lr,ii))
      dd=dd.replace('aaaXPOSaaa',str(xpos))
      dd=dd.replace('aaaYPOSaaa',str(ypos))
      dd=dd.replace('aaaLEDSIZEaaa','10')
      dd=dd.replace('aaaOPIFILEaaa','/CLAS12_Share/apps/caenHvApp/status_channel_led_small.opi')
      print dd
      xpos += 10
    ypos += 10
  ypos += 5



print tail


