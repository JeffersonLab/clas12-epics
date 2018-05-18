#!/usr/bin/env python
import math,sys

PREFIX='B_DET_RICH_HV'

HEAD='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <TYPE>4527</TYPE>
    <DET>RICH</DET>
  </macros>
  <wuid>6ed2d5b9:150f8592e9f:-7fc7</wuid>
  <boy_version>3.2.16.20140409</boy_version>
  <scripts />
  <show_ruler>true</show_ruler>
  <height>700</height>
  <name></name>
  <snap_to_geometry>true</snap_to_geometry>
  <show_grid>false</show_grid>
  <background_color>
    <color name="Header_Background" red="0" green="0" blue="0" />
  </background_color>
  <foreground_color>
    <color red="0" green="0" blue="0" />
  </foreground_color>
  <widget_type>Display</widget_type>
  <show_close_button>true</show_close_button>
  <width>700</width>
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
LINK='''
  <widget typeId="org.csstudio.opibuilder.widgets.linkingContainer" version="1.0.0">
    <opi_file>/CLAS12_Share/apps/mpodLvApp/mpod8008l_channel_expert.opi</opi_file>
    <border_style>0</border_style>
    <tooltip></tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-343e4e6c:151a6497e67:-622b</wuid>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <macros>
      <include_parent_macros>true</include_parent_macros>
      <P>^^^PV^^^</P>
      <C>0</C>
    </macros>
    <resize_behaviour>2</resize_behaviour>
    <visible>true</visible>
    <group_name></group_name>
    <border_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </border_color>
    <widget_type>Linking Container</widget_type>
    <background_color>
      <color name="Header_Background" red="50" green="50" blue="50" />
    </background_color>
    <width>921</width>
    <x>0</x>
    <name>Linking Container_3</name>
    <y>^^^YPOS^^^</y>
    <foreground_color>
      <color red="192" green="192" blue="192" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
'''

TAIL='''
</display>
'''
def genLinks(xoff,yoff,numChannels):
	x=xoff
	y=yoff
	for i in range(numChannels):
        	asdf = LINK
        	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
        	asdf=asdf.replace('^^^PV^^^','B_HW_LVRICH_CH%d'%(i))
        	print asdf
		y+=20
		

print HEAD
genLinks(5,75,35)
print TAIL
