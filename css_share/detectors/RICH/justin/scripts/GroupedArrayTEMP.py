#!/usr/bin/env python
import math,sys

PREFIX='B_DET_RICH_TEMP'

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

TAIL='''
</display>
'''

REC='''
 <widget typeId="org.csstudio.opibuilder.widgets.Rectangle" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <line_width>0</line_width>
    <horizontal_fill>true</horizontal_fill>
    <alarm_pulsing>false</alarm_pulsing>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>71784152:1557935cdbd:-6328</wuid>
    <transparent>false</transparent>
    <pv_value />
    <alpha>255</alpha>
    <bg_gradient_color>
      <color red="255" green="255" blue="255" />
    </bg_gradient_color>
    <scripts>
      <path pathString="set_color_temp.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">$(pv_name)</pv>
      </path>
    </scripts>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <height>^^^HEIGHT^^^</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>^^^PREFIX^^^_SEC1_ROW^^^ROW^^^_PANEL^^^COLUMN^^^</pv_name>
    <gradient>false</gradient>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <anti_alias>true</anti_alias>
    <line_style>0</line_style>
    <widget_type>Rectangle</widget_type>
    <fg_gradient_color>
      <color red="255" green="255" blue="255" />
    </fg_gradient_color>
    <backcolor_alarm_sensitive>true</backcolor_alarm_sensitive>
    <background_color>
      <color name="Off" red="60" green="100" blue="60" />
    </background_color>
    <width>^^^WIDTH^^^</width>
    <x>^^^XPOS^^^</x>
    <name>Rectangle</name>
    <y>^^^YPOS^^^</y>
    <fill_level>0.0</fill_level>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>../../alarms/aiaocalc_alarm_set.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <sig>$(pv_name)</sig>
        </macros>
        <replace>2</replace>
        <description></description>
      </action>
      <action type="EXECUTE_CMD">
        <command>stripTool.sh $(pv_name)</command>
        <command_directory>$(user.home)</command_directory>
        <wait_time>10</wait_time>
        <description>Strip Chart</description>
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
  
LINE='''
  <widget typeId="org.csstudio.opibuilder.widgets.polyline" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <line_width>1</line_width>
    <horizontal_fill>true</horizontal_fill>
    <alarm_pulsing>false</alarm_pulsing>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <arrows>0</arrows>
    <rules />
    <enabled>true</enabled>
    <wuid>46eb8ea1:155971d96f7:-79e2</wuid>
    <transparent>false</transparent>
    <points>
      <point x="258" y="42" />
      <point x="258" y="61" />
      <point x="258" y="61" />
      <point x="258" y="61" />
    </points>
    <fill_arrow>true</fill_arrow>
    <pv_value />
    <alpha>255</alpha>
    <rotation_angle>0.0</rotation_angle>
    <scripts />
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name></pv_name>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <anti_alias>true</anti_alias>
    <line_style>0</line_style>
    <arrow_length>20</arrow_length>
    <widget_type>Polyline</widget_type>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="30" green="144" blue="255" />
    </background_color>
    <width>1</width>
    <x>^^^XL^^^</x>
    <name>Polyline</name>
    <y>^^^YPOS^^^</y>
    <fill_level>0.0</fill_level>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
 '''
 
		
def genRec(x,y,w,h,rowcount,panelnum):
	asdf = REC
	asdf=asdf.replace('^^^HEIGHT^^^','%d'%(h))
	asdf=asdf.replace('^^^WIDTH^^^','%d'%(w))
	asdf=asdf.replace('^^^XPOS^^^','%d'%(x))
	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
	asdf=asdf.replace('^^^ROW^^^','%d'%(rowcount+1))
	asdf=asdf.replace('^^^COLUMN^^^','%d'%(panelnum))
	asdf=asdf.replace('^^^PREFIX^^^',PREFIX)
	print asdf
	
def genLine(x,y):
	asdf = LINE
	asdf=asdf.replace('^^^XL^^^','%d'%(x))
	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
	print asdf

def genSector(xoff,yoff):
	
	a = [[2,3,3,3,3,3,3,3,3,2],
		[3,3,3,3,3,3,3,3,3],
		[2,3,3,3,3,3,3,3,3],
		[2,3,3,3,3,3,3,3,2],
		[3,3,3,3,3,3,3,3],
		[2,3,3,3,3,3,3,3],
		[2,3,3,3,3,3,3,2],
		[3,3,3,3,3,3,3],
		[2,3,3,3,3,3,3],
		[2,3,3,3,3,3,2],
		[3,3,3,3,3,3],
		[2,3,3,3,3,3],
		[2,3,3,3,3,2],
		[3,3,3,3,3],
		[2,3,3,3,3],
		[2,3,3,3,2],
		[3,3,3,3],
		[2,3,3,3],
		[2,3,3,2],
		[3,3,3],
		[3,2,3],
		[2,3,2],
		[3,3]]
		
	x = xoff
	y = yoff
	h = 15
	rowcount=0
	widthPMT = 15
	panelnum=1
	
	for i in a:
		for j in i:
			if j == 2:
				w = 2*widthPMT
				genRec(x,y,w,h,rowcount,panelnum)
				#genLine(x+widthPMT,y)
				x+=w+5
			if j==3:
				w=3*widthPMT
				genRec(x,y,w,h,rowcount,panelnum)
				#genLine(x+widthPMT,y)
				#genLine(x+2*widthPMT,y)
				x+=w+5
			panelnum+=1
		y+=h+5
		x=xoff+(rowcount+1)*(widthPMT+1)/2
		rowcount+=1
		panelnum=1


print HEAD
genSector(100,100)
print TAIL
