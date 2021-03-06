#!/usr/bin/env python
import math

head='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <macros>
    <include_parent_macros>true</include_parent_macros>
  </macros>
  <wuid>-1440ecc8:14f850aa82a:-67a8</wuid>
  <boy_version>3.2.16.20140409</boy_version>
  <scripts />
  <show_ruler>true</show_ruler>
  <height>550</height>
  <name></name>
  <snap_to_geometry>true</snap_to_geometry>
  <show_grid>false</show_grid>
  <background_color>
    <color name="Read_Background" red="77" green="77" blue="77" />
  </background_color>
  <foreground_color>
    <color red="192" green="192" blue="192" />
  </foreground_color>
  <widget_type>Display</widget_type>
  <show_close_button>false</show_close_button>
  <width>550</width>
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


rdbk='''
  <widget typeId="org.csstudio.opibuilder.widgets.TextUpdate" version="1.0.0">
    <border_style>14</border_style>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <alarm_pulsing>false</alarm_pulsing>
    <precision>0</precision>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>43c131e0:159e1500e62:-7fb3</wuid>
    <transparent>false</transparent>
    <pv_value />
    <auto_size>false</auto_size>
    <text>##.###</text>
    <rotation_angle>0.0</rotation_angle>
    <scripts />
    <border_alarm_sensitive>true</border_alarm_sensitive>
    <show_units>false</show_units>
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <pv_name>___PV___</pv_name>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color name="Write_Foreground" />
    </border_color>
    <precision_from_pv>false</precision_from_pv>
    <widget_type>Text Update</widget_type>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <wrap_words>false</wrap_words>
    <format_type>1</format_type>
    <background_color>
      <color name="Read_Background" red="77" green="77" blue="77" />
    </background_color>
    <width>60</width>
    <x>___XPOS___</x>
    <name>Text Update</name>
    <y>___YPOS___</y>
    <foreground_color>
      <color name="Read_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <font>
      <opifont.name fontName="Sans" height="8" style="0">Fine Print</opifont.name>
    </font>
  </widget>
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
    <height>20</height>
    <name>Linking Container</name>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <opi_file>status_channel_led.opi</opi_file>
    <foreground_color>
      <color red="192" green="192" blue="192" />
    </foreground_color>
    <background_color>
      <color red="77" green="77" blue="77" />
    </background_color>
    <group_name></group_name>
    <enabled>true</enabled>
    <widget_type>Linking Container</widget_type>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
    <width>20</width>
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


radD=230
radU=200

xoff=100
yoff=100

x0=xoff+radD
y0=yoff+radD

print head

iy=0

for ii in range(1,49):

  #angle = float(ii-1)*2*math.pi/48

  rD=radD+30
  rU=radU

  angle = float(ii-1)*2*math.pi/24
  angle = float(ii-1)*2*math.pi/48

  #dy = -80*math.sin(angle)
  dx =  30*math.fabs(math.sin(angle))
  if math.cos(angle)<0: dx *= -1

#  if ii%2==1:
#    rU = rU - 15

  #if ii>24:
  #  angle += math.pi/24

  xposD = x0 - rD*math.cos(angle) - dx
  yposD = y0 + iy*22 #- rD*math.sin(angle) + dy
  xposU = x0 - rU*math.cos(angle) + dx
  yposU = y0 + iy*22 #- rU*math.sin(angle) + dy

  if   ii<=12: iy -= 1
  elif ii<=36: iy += 1
  else:        iy -= 1


  dd=rdbk
  dd=dd.replace('___PV___', 'B_DET_CTOF_FADC_D%.2d:c1' % (ii))
  dd=dd.replace('___XPOS___',str(int(xposD)))
  dd=dd.replace('___YPOS___',str(int(yposD)))
  dd=dd.replace('___SIZE___','20')

  uu=rdbk
  uu=uu.replace('___PV___', 'B_DET_CTOF_FADC_U%.2d:c1' % (ii))
  uu=uu.replace('___XPOS___',str(int(xposU)))
  uu=uu.replace('___YPOS___',str(int(yposU)))
  uu=uu.replace('___SIZE___','20')

  print dd
  print uu

print tail


