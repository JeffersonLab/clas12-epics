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
    <pv_name>B_HW_FEVME1_Sl^^^SLOTNUM^^^_Fi^^^FIBNUM^^^:$(SCREEN)</pv_name>
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
 
		
def genRec(x,y,w,h,slot,Fi):
	asdf = REC
	asdf=asdf.replace('^^^HEIGHT^^^','%d'%(h))
	asdf=asdf.replace('^^^WIDTH^^^','%d'%(w))
	asdf=asdf.replace('^^^XPOS^^^','%d'%(x))
	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
	asdf=asdf.replace('^^^SLOTNUM^^^','%02d'%(slot))
	asdf=asdf.replace('^^^FIBNUM^^^','%02d'%(Fi))
	asdf=asdf.replace('^^^PREFIX^^^',PREFIX)
	print asdf

def genLine(x,y):
	asdf = LINE
	asdf=asdf.replace('^^^XL^^^','%d'%(x))
	asdf=asdf.replace('^^^YPOS^^^','%d'%(y))
	print asdf

def genSector(xoff,yoff):
#0x(Size)(Sl)(Fi)	
	a = [[0x270D,0x370E,0x3704,0x3705,0x3706,0x3707,0x3700,0x3701,0x3702,0x2703],
		[0x370C,0x361C,0x361D,0x361E,0x361F,0x3618,0x3619,0x361A,0x361B],
		[0x2709,0x3614,0x3615,0x3616,0x3617,0x3610,0x3611,0x3612,0x3613],
		[0x2708,0x360C,0x360D,0x360E,0x360F,0x3608,0x3609,0x360A,0x260B],
		[0x3604,0x3605,0x3606,0x3607,0x3600,0x3601,0x3602,0x3603],
		[0x251C,0x351D,0x351E,0x351F,0x3518,0x3519,0x351A,0x351B],
		[0x2514,0x3515,0x3516,0x3517,0x3510,0x3511,0x3512,0x2513],
		[0x350C,0x350D,0x350E,0x3508,0x3509,0x350A,0x350B],
		[0x2504,0x3505,0x3506,0x3500,0x3501,0x3502,0x3503],
		[0x241B,0x341E,0x341F,0x3414,0x3415,0x3416,0x2417],
		[0x341A,0x341D,0x3410,0x3411,0x3412,0x3413],
		[0x2419,0x341C,0x340C,0x340D,0x340E,0x340F],
		[0x2418,0x340B,0x3404,0x3405,0x3406,0x2407],
		[0x340A,0x3400,0x3401,0x3402,0x3403],
		[0x2409,0x331C,0x331D,0x331E,0x331F],
		[0x2408,0x3318,0x3319,0x331A,0x231B],
		[0x3314,0x3315,0x3316,0x3317],
		[0x2310,0x3311,0x3312,0x3313],
		[0x230C,0x330D,0x330E,0x230F],
		[0x3308,0x3309,0x330A],
		[0x3304,0x2305,0x3306],
		[0x2302,0x3303,0x2307],
		[0x3300,0x3301]]
		
	x = xoff
	y = yoff
	h = 20
	rowcount=0
	widthPMT = 20
	panelnum=1
	
	for i in a:
		for j in i:
			Fi = (0xFF & j)
			sizeslot = (j-Fi)>>8
			slot = (sizeslot & 0xF)
			size = (sizeslot-slot)>>4
			#print size, slot, Fi
			if size == 2:
				w = 2*widthPMT
				genRec(x,y,w,h,slot,Fi)
				#genLine(x+widthPMT,y)
			
				x+=w+3
			if size==3:
				w=3*widthPMT
				genRec(x,y,w,h,slot,Fi)
				#genLine(x+widthPMT,y)
				#genLine(x+2*widthPMT,y)
				x+=w+3
			panelnum+=1
		y+=h+3
		x=xoff+(rowcount+1)*(widthPMT+1)/2
		rowcount+=1
		panelnum=1


print HEAD
genSector(10,10)
print TAIL
