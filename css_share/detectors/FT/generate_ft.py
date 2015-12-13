#!/usr/bin/env python
import math,sys

HEAD='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <macros>
    <include_parent_macros>true</include_parent_macros>
    <P>B_DET_FT_HV</P>
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
    <scripts>
      <path pathString="../../apps/caenHvApp/set_status_color.js" checkConnect="true" sfe="false" seoe="false">
        <pv trig="true">$(P).L</pv>
        <pv trig="true">$(P).T</pv>
      </path>
    </scripts>
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
WIDGPT='''    <point x="aaaXPOSaaa" y="aaaYPOSaaa" />'''
WIDGTAIL='''
    </points>

    <actions hook="true" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>/CLAS12_Share/apps/caenHvApp/det_channel_novice_withheader.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(P)_QaaaQUADRANTaaaGaaaGROUPaaa</P>
        </macros>
        <replace>2</replace>
        <description>Open Controls</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>$(P)_QaaaQUADRANTaaaGaaaGROUPaaa:switch</pv_name>
        <value>1</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn On</description>
      </action>
      <action type="WRITE_PV">
        <pv_name>$(P)_QaaaQUADRANTaaaGaaaGROUPaaa:switch</pv_name>
        <value>0</value>
        <timeout>10</timeout>
        <confirm_message></confirm_message>
        <description>Turn Off</description>
      </action>
    </actions>

    <transparent>false</transparent>
    <pv_name>$(P)_QaaaQUADRANTaaaGaaaGROUPaaa:switch:fbk</pv_name>
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
    <height>aaaHEIGHTaaa</height>
    <width>aaaWIDTHaaa</width>
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
    <y>aaaYPOSaaa</y>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <x>aaaXPOSaaa</x>
  </widget>
'''

globoff=[500,500]
off=0.1
scale=20

polygons=[
    [ [0+off,4+off],[2-off,4+off],[2-off,7-off],[1-off,7-off],[1-off,11-off],[0+off,11-off] ],
    [ [2+off,3+off],[3-off,3+off],[3-off,9-off],[2-off,9-off],[2-off,11-off],[1+off,11-off],[1+off,7+off],[2+off,7+off] ],
    [ [3+off,2+off],[4-off,2+off],[4-off,10-off],[3-off,10-off],[3-off,11-off],[2+off,11-off],[2+off,9+off],[3+off,9+off] ],
    [ [4+off,0+off],[5-off,0+off],[5-off,10-off],[4+off,10-off] ],
    [ [5+off,0+off],[6-off,0+off],[6-off,10-off],[5+off,10-off] ],
    [ [6+off,0+off],[7-off,0+off],[7-off,9-off],[6+off,9-off] ],
    [ [7+off,0+off],[8-off,0+off],[8-off,8-off],[7+off,8-off] ],
    [ [8+off,0+off],[9-off,0+off],[9-off,7-off],[8+off,7-off] ],
    [ [9+off,0+off],[11-off,0+off],[11-off,3-off],[10-off,3-off],[10-off,6-off],[9+off,6-off]]
]

def genQuadrant(quadrant):
  if quadrant%2==0:  group=1
  else:              group=9
  for points in polygons:
    print WIDGHEAD
    ymin,xmin=99999,99999
    ymax,xmax=-99999,-99999
    for point in points:

      xx=scale*point[0]
      yy=scale*point[1]
      if quadrant==3 or quadrant==2: xx *= -1
      if quadrant==1 or quadrant==2: yy *= -1

      pt=WIDGPT
      pt=pt.replace('aaaXPOSaaa','%d'%(xx))
      pt=pt.replace('aaaYPOSaaa','%d'%(yy))
      if xx>xmax: xmax=xx
      if xx<xmin: xmin=xx
      if yy>ymax: ymax=yy
      if yy<ymin: ymin=yy
      print pt,
    height=ymax-ymin
    width=xmax-xmin
    asdf=WIDGTAIL
    asdf=asdf.replace('aaaHEIGHTaaa','%d'%(height))
    asdf=asdf.replace('aaaWIDTHaaa','%d'%(width))
    asdf=asdf.replace('aaaXPOSaaa','%d'%(globoff[0]+xmin))
    asdf=asdf.replace('aaaYPOSaaa','%d'%(globoff[1]+ymin))
    asdf=asdf.replace('aaaGROUPaaa','%d'%(group))
    asdf=asdf.replace('aaaQUADRANTaaa','%d'%(quadrant))
    print asdf
    if quadrant%2==0: group += 1
    else:             group -= 1


print HEAD
for qq in range(1,5):
  genQuadrant(qq)
print TAIL

