#!/usr/bin/env python

head='''
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <show_close_button>true</show_close_button>
  <rules />
  <wuid>2da4dada:138bb0b2666:-7ff6</wuid>
  <show_grid>true</show_grid>
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <scripts />
  <height>600</height>
  <macros>
    <include_parent_macros>true</include_parent_macros>
  </macros>
  <boy_version>4.0.104.201511041839</boy_version>
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
  <grid_space>6</grid_space>
  <show_ruler>true</show_ruler>
  <y>-1</y>
  <snap_to_geometry>true</snap_to_geometry>
  <foreground_color>
    <color name="GRID" red="90" green="90" blue="90" />
  </foreground_color>
  <actions hook="false" hook_all="false" />
'''
tail='''
</display>
'''
widget='''
  <widget typeId="org.csstudio.opibuilder.widgets.linkingContainer" version="1.0.0">
    <opi_file>leakageCurrents.opi</opi_file>
    <border_style>0</border_style>
    <tooltip></tooltip>
    <rules />
    <enabled>true</enabled>
    <wuid>-7c93f1e6:15aa8aa55d8:-7f87</wuid>
    <scripts />
    <height>16</height>
    <border_width>1</border_width>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <macros>
      <include_parent_macros>true</include_parent_macros>
      <L>---L---</L>
      <P>---P---</P>
    </macros>
    <resize_behaviour>2</resize_behaviour>
    <visible>true</visible>
    <group_name></group_name>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <widget_type>Linking Container</widget_type>
    <background_color>
      <color name="OPI_Background" red="50" green="50" blue="50" />
    </background_color>
    <width>294</width>
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

prefix='B_SVT_HV_'
nSensorsPerRegion={1:10,2:14,3:18,4:24}
slotsChansPerRegion={1:{7:16,8:4,9:16,10:12},
                     2:{9:16,10:12},
                     3:{8:16,9:16,10:4},
		     4:{8:16,9:16,10:16}}
WW=[]
Y=0
for region in [1,2,3,4]:
  sensor=1
  for slot in range(20):
    isensor=0
    if not slotsChansPerRegion[region].has_key(slot): continue
    for ii in range(slotsChansPerRegion[region][slot]):
      for tb in ['T','B']:
        L='R'+str(region)+'S'+str(sensor)+tb
	P=prefix+L+'_Slot'+str(slot)
	#print ii,isensor,nSensorsPerRegion[region],slotsChansPerRegion[region][slot],P
	W=widget
	W=W.replace('---L---',L)
	W=W.replace('---P---',P)
	W=W.replace('---X---','0')
	W=W.replace('---Y---',str(Y))
	WW.append(W)
	Y+=18
	isensor+=1
      sensor+=1
      if isensor>=slotsChansPerRegion[region][slot]: break
      if sensor>nSensorsPerRegion[region]: break 
    if sensor>nSensorsPerRegion[region]: break 

print head
for ww in WW: print ww
print tail

