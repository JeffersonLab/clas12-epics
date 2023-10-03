#!/usr/bin/env python3
import sys,argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

cli = argparse.ArgumentParser(description='CS-Studio BOB to OPI converter')
cli.add_argument('input',help='path to .bob file')
cli.add_argument('-d',help='delete unknown widget types',default=False,action='store_true')
args = cli.parse_args(sys.argv[1:])

root = ET.parse(args.input).getroot()
root.set('typeId','org.csstudio.opibuilder.Display')

widget_types = {
    'textentry':'org.csstudio.opibuilder.widgets.TextInput',
    'textupdate':'org.csstudio.opibuilder.widgets.TextUpdate',
    'bool_button':'org.csstudio.opibuilder.widgets.BoolButton',
    'action_button':'org.csstudio.opibuilder.widgets.ActionButton',
    'meter':'org.csstudio.opibuilder.widgets.Meter',
    'label':'org.csstudio.opibuilder.widgets.Label',
    'spinner':'org.csstudio.opibuilder.widgets.spinner',
    'tank':'org.csstudio.opibuilder.widgets.tank',
    'scrollbar':'org.csstudio.opibuilder.widgets.ScrollBar',
    #'choice':'org.csstudio.opibuilder.widgets.ChoiceButton',
    'choice':'org.csstudio.opibuilder.widgets.MenuButton',
    'led':'org.csstudio.opibuilder.widgets.LED',
    'rectangle':'org.csstudio.opibuilder.widgets.Rectangle',
    'group':'org.csstudio.opibuilder.widgets.groupingContainer',
    'combo':'org.csstudio.opibuilder.widgets.combo',
    'polyline':'org.csstudio.opibuilder.widgets.polyline',
    'picture':'org.csstudio.opibuilder.widgets.Image',
    'slide_button':'org.csstudio.opibuilder.widgets.BoolButton'
    #'slide_button':'org.csstudio.opibuilder.widgets.scaledslider'
    # don't work or untested: 
    #'stripchart':'org.csstudio.opibuilder.widgets.StripChart',
    #'byte_monitor':'org.csstudio.opibuilder.widgets.ByteMonitor',
    #'thermometer':'org.csstudio.opibuilder.widgets.Thermometer',
    #'gauge':'org.csstudio.opibuilder.widgets.Gauge',
}

removals = set()

# recursive function to modify all sub-widgets:
def munge(widget):
  for w in widget.findall('pv_name'):
    w.text = w.text.replace('pva://','')
  for w in widget.findall('widget'):
    # polyline points must be ints in cs-studio:
    if w.get('type') == 'polyline':
      for points in w.findall('points'):
        for p in points.findall('point'):
          p.set('x','%d'%float(p.get('x')))
          p.set('y','%d'%float(p.get('y')))
    # cs-studio requires the class name:
    if w.get('type') in widget_types:
      w.set('typeId',widget_types[w.get('type')])
    # remove unknown widget types:
    elif args.d:
      removals.add(w.get('type'))
      widget.remove(w)
    else:
      sys.exit('Unknown widget type:  '+w.get('type'))
    munge(w)

munge(root)

# put the darn encoding line back at the top:
for line in minidom.parseString(ET.tostring(root)).toprettyxml(indent='  ',encoding='utf-8').decode('utf-8').split('\n'):
  if len(line.strip()) != 0:
    print(line)

if args.d:
  print('\n\n<!--\nREMOVALS:\n'+'\n'.join(removals)+'\n-->')

