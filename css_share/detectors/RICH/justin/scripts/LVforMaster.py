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
TEXTUPDATE='''
  <widget typeId="org.csstudio.opibuilder.widgets.TextUpdate" version="1.0.0">
    <border_style>1</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <alarm_pulsing>false</alarm_pulsing>
    <precision>0</precision>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <horizontal_alignment>0</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>3760820c:156e6cc1c51:-6550</wuid>
    <transparent>false</transparent>
    <pv_value />
    <auto_size>false</auto_size>
    <text>##.###</text>
    <rotation_angle>0.0</rotation_angle>
    <scripts />
    <border_alarm_sensitive>true</border_alarm_sensitive>
    <show_units>true</show_units>
    <height>17</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>^^^PV^^^</pv_name>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="255" green="255" blue="255" />
    </border_color>
    <precision_from_pv>true</precision_from_pv>
    <widget_type>Text Update</widget_type>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <wrap_words>false</wrap_words>
    <format_type>0</format_type>
    <background_color>
      <color name="Read_Background" red="77" green="77" blue="77" />
    </background_color>
    <width>60</width>
    <x>^^^XPOS^^^</x>
    <name>Text Update</name>
    <y>^^^YPOS^^^</y>
    <foreground_color>
      <color red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
'''

LABEL='''
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>1</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>0</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>3760820c:156e6cc1c51:-6413</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>^^^CHAN^^^</text>
    <scripts />
    <height>17</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="255" green="255" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>20</width>
    <x>^^^XPOS^^^</x>
    <name>Label</name>
    <y>^^^YPOS^^^</y>
    <foreground_color>
      <color name="Read_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/detectors/RICH/RICH_LV_Novice_Individual.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>^^^PV^^^</P>
          <C>0</C>
        </macros>
        <replace>2</replace>
        <description>Open Controls</description>
      </action>
    </actions>
    <show_scrollbar>false</show_scrollbar>
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
	width1=20
	width2=60
	for i in range(numChannels):
		for j in range(3):
			if j ==0:
				asdf = LABEL
      			        asdf=asdf.replace('^^^CHAN^^^','%d'%(i))
				asdf=asdf.replace('^^^XPOS^^^','%d'%(x))
                                asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
				asdf=asdf.replace('^^^PV^^^','B_HW_LVRICH_CH%d'%(i))
				print asdf
			if j == 1:
        			asdf = TEXTUPDATE
				asdf=asdf.replace('^^^XPOS^^^','%d'%(x+width1))	
        			asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
        			asdf=asdf.replace('^^^PV^^^','B_HW_LVRICH_CH%d:v_sens'%(i))
        			print asdf
			if j ==2:
				asdf = TEXTUPDATE
                                asdf=asdf.replace('^^^XPOS^^^','%d'%(x+width1+width2))
                                asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
                                asdf=asdf.replace('^^^PV^^^','B_HW_LVRICH_CH%d:i_rd'%(i))
                                print asdf
		y+=17
		

print HEAD
genLinks(3,3,35)
print TAIL
