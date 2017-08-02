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

WIDGHEAD='''
  <widget typeId="org.csstudio.opibuilder.widgets.Rectangle" version="1.0.0">
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <visible>true</visible>
    <fill_level>0.0</fill_level>
    <line_color>
      <color red="128" green="0" blue="255" />
    </line_color>
    <wuid>6ed2d5b9:150f8592e9f:-7e38</wuid>
    <rotation_angle>0.0</rotation_angle>
    <anti_alias>true</anti_alias>
    <name>Rectangle</name>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <alpha>255</alpha>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <points>
'''

WIDGPT='''    <point x="^^^XPOS^^^" y="^^^YPOS^^^" />
'''

WIDGTAIL='''
    </points>

    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^</P>
        </macros>
        <replace>2</replace>
        <description>Open Controls</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^:pwonoff</pv_name>
        <value>1</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn On</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^:pwonoff</pv_name>
        <value>0</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn Off</description>
      </action>
    </actions>

    <scripts>
      <path pathString="../../apps/caenHvApp/set_status_led2.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^.L</pv>
        <pv trig="true">^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^.T</pv>
      </path>
    </scripts>
    <transparent>false</transparent>
    <pv_name>^^^PREFIX^^^_ROW^^^ROW^^^_COL^^^COLUMN^^^_NUM_^^^NUMBER^^^</pv_name>
    <background_color>
      <color name="Off" red="60" green="100" blue="60" />
    </background_color>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <widget_type>Rectangle</widget_type>
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

TAIL='''
</display>
'''

def genTriangle(offx, offy):
	
	x=offx
	y=offy
	diff=3
	h=18
	w=18
	k=28
	num=1
	
	for j in range(23):
		for i in range(k):
			print WIDGHEAD
			pt = WIDGPT
			pt=pt.replace('^^^XPOS^^^','%d'%(x))
			pt=pt.replace('^^^YPOS^^^','%d'%(y))
			print pt
			asdf = 	WIDGTAIL
			asdf=asdf.replace('^^^HEIGHT^^^','%d'%(h))
			asdf=asdf.replace('^^^WIDTH^^^','%d'%(w))
			asdf=asdf.replace('^^^XPOS^^^','%d'%(x))
			asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
			asdf=asdf.replace('^^^ROW^^^','%d'%(j+1))
			asdf=asdf.replace('^^^COLUMN^^^','%d'%(i+1))
			asdf=asdf.replace('^^^NUMBER^^^','%d'%(num))
			asdf=asdf.replace('^^^PREFIX^^^',PREFIX)
			print asdf
			num+=1
			x+=w+diff
		k-=1
		y+=h+diff		
		x=offx+(j+1)*(h+diff)/2

print HEAD
genTriangle(100,100)
print TAIL