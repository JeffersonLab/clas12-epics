#!/usr/bin/env python

HEAD='''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <show_close_button>true</show_close_button>
  <rules />
  <wuid>2da4dada:138bb0b2666:-7ff6</wuid>
  <show_grid>false</show_grid>
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <scripts />
  <height>900</height>
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
  <width>1400</width>
  <x>-1</x>
  <name>IOC Health</name>
  <grid_space>5</grid_space>
  <show_ruler>true</show_ruler>
  <y>-1</y>
  <snap_to_geometry>true</snap_to_geometry>
  <foreground_color>
    <color name="GRID" red="90" green="90" blue="90" />
  </foreground_color>
  <actions hook="false" hook_all="false" />
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>0</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>288a8579:14fa40063a5:-7335</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>IOC Health</text>
    <scripts />
    <height>25</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>173</width>
    <x>18</x>
    <name>Label</name>
    <y>12</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="14" style="1">Header 2</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-6fea</wuid>
    <transparent>false</transparent>
    <auto_size>false</auto_size>
    <text>Autosave</text>
    <scripts />
    <height>508</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>0</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color name="Read_Background" red="77" green="77" blue="77" />
    </background_color>
    <width>505</width>
    <x>881</x>
    <name>Label_12</name>
    <y>47</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-7700</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>IOC Name</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>121</width>
    <x>0</x>
    <name>Label_7</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-76b5</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Hostname</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>133</width>
    <x>120</x>
    <name>Label_7</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-76a1</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Up Time</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>127</width>
    <x>252</x>
    <name>Label_7</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-7697</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Heartbeat</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>105</width>
    <x>378</x>
    <name>Label_7</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-7690</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Expert</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>55</width>
    <x>478</x>
    <name>Label_10</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-767f</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Last Reboot</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>133</width>
    <x>622</x>
    <name>Label_12</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-7675</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Status</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>85</width>
    <x>867</x>
    <name>Label_12</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-766b</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Message</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>181</width>
    <x>957</x>
    <name>Label_14</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-765f</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Recently</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>199</width>
    <x>1149</x>
    <name>Label_14</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>57940341:15024427454:-7381</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Expert</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>55</width>
    <x>1322</x>
    <name>Label_10</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-16fff77:1575ddfa353:-5bb4</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>Console</text>
    <scripts />
    <height>20</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>55</width>
    <x>752</x>
    <name>Label_13</name>
    <y>66</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-16fff77:1575ddfa353:-5bb3</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>  Hard
Reboot</text>
    <scripts />
    <height>38</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>94</width>
    <x>795</x>
    <name>Label_14</name>
    <y>49</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <border_style>0</border_style>
    <tooltip></tooltip>
    <horizontal_alignment>1</horizontal_alignment>
    <rules />
    <enabled>true</enabled>
    <wuid>-16fff77:1575ddfa353:-5ba6</wuid>
    <transparent>true</transparent>
    <auto_size>false</auto_size>
    <text>  Soft
Reboot</text>
    <scripts />
    <height>38</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <visible>true</visible>
    <vertical_alignment>1</vertical_alignment>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Label</widget_type>
    <wrap_words>true</wrap_words>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <width>94</width>
    <x>522</x>
    <name>Label_19</name>
    <y>49</y>
    <foreground_color>
      <color name="Header_Foreground" red="255" green="255" blue="255" />
    </foreground_color>
    <actions hook="false" hook_all="false" />
    <show_scrollbar>false</show_scrollbar>
    <font>
      <opifont.name fontName="Sans" height="10" style="0">Default</opifont.name>
    </font>
  </widget>
'''

SOFTIOC='''
  <widget typeId="org.csstudio.opibuilder.widgets.linkingContainer" version="1.0.0">
    <opi_file>---OPI---</opi_file>
    <border_style>1</border_style>
    <tooltip></tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-143daf8a:1501f573c2a:-75c3</wuid>
    <scripts />
    <height>---H---</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <macros>
      <include_parent_macros>true</include_parent_macros>
      <ioc>---IOC---</ioc>
    </macros>
    <resize_behaviour>1</resize_behaviour>
    <visible>true</visible>
    <group_name></group_name>
    <border_color>
      <color name="OPI_Background" red="50" green="50" blue="50" />
    </border_color>
    <widget_type>Linking Container</widget_type>
    <background_color>
      <color name="OPI_Background" red="50" green="50" blue="50" />
    </background_color>
    <width>---W---</width>
    <x>---X---</x>
    <name>Linking Container</name>
    <y>---Y---</y>
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

X0=0
Y0=86
W0=1386
H0=23
OPI0='ioc_chan_soft_light_autosave.opi'
IOCLIST='lists/ioc_all.txt'

print HEAD

yy=Y0
for ioc in open(IOCLIST,'r').readlines():
  ioc=ioc.strip().split()[0]
  oo=SOFTIOC
  oo=oo.replace('---X---',str(X0))
  oo=oo.replace('---Y---',str(yy))
  oo=oo.replace('---W---',str(W0))
  oo=oo.replace('---H---',str(H0))
  oo=oo.replace('---OPI---',OPI0)
  oo=oo.replace('---IOC---',ioc)
  print oo
  yy+=H0+1

print TAIL

