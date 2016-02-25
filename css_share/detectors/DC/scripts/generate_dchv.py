#!/usr/bin/env python
import math,sys

PREFIX='B_DET_DC_HV'

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
  <width>800</width>
  <x>-1</x>
  <name>Display</name>
  <grid_space>5</grid_space>
  <show_ruler>true</show_ruler>
  <y>-1</y>
  <snap_to_geometry>false</snap_to_geometry>
  <foreground_color>
    <color name="GRID" red="90" green="90" blue="90" />
  </foreground_color>
  <actions hook="false" hook_all="false" />
'''

RECT='''<widget typeId="org.csstudio.opibuilder.widgets.Rectangle" version="1.0.0">
    <border_style>0</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <line_width>0</line_width>
    <horizontal_fill>true</horizontal_fill>
    <alarm_pulsing>false</alarm_pulsing>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-210bc071:152a8b02736:-7faa</wuid>
    <transparent>false</transparent>
    <pv_value />
    <alpha>255</alpha>
    <bg_gradient_color>
      <color red="255" green="255" blue="255" />
    </bg_gradient_color>
    <scripts>
      <path pathString="/CLAS12_Share/apps/caenHvApp/set_status_color.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">$(P).L</pv>
        <pv trig="true">$(P).T</pv>
      </path>
    </scripts>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <height>___HEIGHT___</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name></pv_name>
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
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="30" green="144" blue="255" />
    </background_color>
    <width>___WIDTH___</width>
    <x>___XXX___</x>
    <name>Rectangle</name>
    <y>___YYY___</y>
    <fill_level>0.0</fill_level>
    <foreground_color>
      <color red="255" green="0" blue="0" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
    <line_color>
      <color red="128" green="0" blue="255" />
    </line_color>
    <pv_name>___PV___</pv_name>
    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>___PV___</P>
        </macros>
        <replace>2</replace>
        <description>Open Controls</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>___PV___:pwonoff</pv_name>
        <value>1</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn On</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>___PV___:pwonoff</pv_name>
        <value>0</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn Off</description>
      </action>
    </actions>
  </widget>
'''

TAIL='''
</display>
'''

SWIRES=['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
FWIRES=['01-08','09-16','17-24','25-32','33-48','49-64','65-80','81-112']
GWIRES=['01-32','33-112']
WIRES={'S':SWIRES,'F':FWIRES,'G':GWIRES}
WIDTH=10
HEIGHT=20
GAP=2

def genSector(sector,x0,y0):
  xx=x0
  for reg in [1,2,3]:
    for slay in [1,2]:
      for sfg in ['S','F','G']:
        if sector>3:  yy=y0
        else:
          if sfg=='G': yy=y0 + HEIGHT*4 + 3*GAP - HEIGHT
          else:        yy=y0 + HEIGHT*8 + 7*GAP - HEIGHT
        for wires in WIRES[sfg]:
          P=PREFIX+'_SEC'+str(sector)+'_R'+str(reg)+'_SL'+str(slay)+'_'+sfg+wires
          if sfg=='G':
            if wires=='01-32': height=5
            else:              height=3
          else:                height=1
          rect=RECT
          rect=rect.replace('___XXX___',str(xx))
          rect=rect.replace('___YYY___',str(yy))
          rect=rect.replace('___HEIGHT___',str(HEIGHT*height+(height-1)*GAP))
          rect=rect.replace('___WIDTH___',str(WIDTH))
          rect=rect.replace('___PV___',P)
          if sector>3: yy += (HEIGHT+GAP)*height
          else:
            if sfg=='G': yy -= (HEIGHT+GAP)*(height-2)
            else:        yy -= (HEIGHT+GAP)*height
          print rect
        xx += WIDTH+GAP
    xx += GAP*2



print HEAD
for qq in range(1,5):
  genSector(1,50+10,50)
  genSector(2,50+250,50)
  genSector(3,50+490,50)
  genSector(4,50+10,250)
  genSector(5,50+250,250)
  genSector(6,50+490,250)
print TAIL

