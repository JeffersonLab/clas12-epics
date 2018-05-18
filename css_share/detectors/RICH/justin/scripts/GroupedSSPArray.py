#!/usr/bin/env python
import math,sys

PREFIX='B_HW_FEVME'

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
<widget typeId="org.csstudio.opibuilder.widgets.TextUpdate" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>true</forecolor_alarm_sensitive>
    <alarm_pulsing>false</alarm_pulsing>
    <precision>1</precision>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <horizontal_alignment>0</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-3d754df7:15dc82ef14f:-7e66</wuid>
    <transparent>false</transparent>
    <pv_value />
    <auto_size>false</auto_size>
    <text>##.#</text>
    <rotation_angle>0.0</rotation_angle>
    <scripts />
    <border_alarm_sensitive>true</border_alarm_sensitive>
    <show_units>false</show_units>
    <height>^^^HEIGHT^^^</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>B_HW_FEVME1_TILE^^^TILENUM^^^:$(SCREEN)</pv_name>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <precision_from_pv>false</precision_from_pv>
    <widget_type>Text Update</widget_type>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <wrap_words>false</wrap_words>
    <format_type>0</format_type>
    <background_color>
      <color name="Read_Background" red="77" green="77" blue="77" />
    </background_color>
    <width>^^^WIDTH^^^</width>
    <x>^^^XPOS^^^</x>
    <name>Text Update</name>
    <y>^^^YPOS^^^</y>
    <foreground_color>
      <color name="Read_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false">
    </actions>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>

  '''
 
		
def genRec(x,y,w,h,tilenum):
	asdf = REC
	asdf=asdf.replace('^^^HEIGHT^^^','%d'%(h))
	asdf=asdf.replace('^^^WIDTH^^^','%d'%(w))
	asdf=asdf.replace('^^^XPOS^^^','%d'%(x))
	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
	asdf=asdf.replace('^^^TILENUM^^^','%03d'%(tilenum))
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
	h = 20
	rowcount=0
	widthPMT = 20
	tilenum=138
	
	for i in a:
		for j in i:
			#print size, slot, Fi
			if j == 2:
				w = 2*widthPMT
				genRec(x,y,w,h,tilenum)
				#genLine(x+widthPMT,y)
			
				x+=w+3
			if j == 3:
				w=3*widthPMT
				genRec(x,y,w,h,tilenum)
				#genLine(x+widthPMT,y)
				#genLine(x+2*widthPMT,y)
				x+=w+3
			tilenum-=1
		y+=h+3
		x=xoff+(rowcount+1)*(widthPMT+1)/2
		rowcount+=1


print HEAD
genSector(10,10)
print TAIL
