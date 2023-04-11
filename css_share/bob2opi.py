#!/usr/bin/env python3
import sys,argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

cli = argparse.ArgumentParser(description='CS-Studio BOB to OPI converter')
cli.add_argument('input',help='path to .bob file')
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
    'spinner':'org.csstudio.opibuilder.widgets.Spinner',
    'tank':'org.csstudio.opibuilder.widgets.tank',
    'scrollbar':'org.csstudio.opibuilder.widgets.ScrollBar',
    'choice':'org.csstudio.opibuilder.widgets.MenuButton',
    'led':'org.csstudio.opibuilder.widgets.LED'
    #'stripchart':'org.csstudio.opibuilder.widgets.StripChart',
    #'byte_monitor':'org.csstudio.opibuilder.widgets.ByteMonitor',
    #'thermometer':'org.csstudio.opibuilder.widgets.Thermometer',
    #'gauge':'org.csstudio.opibuilder.widgets.Gauge',
    #'combo':'org.csstudio.opibuilder.widgets.Combo',
}

for widget in root.iter('widget'):
  if widget.get('type') in widget_types:
    widget.set('typeId',widget_types[widget.get('type')])
  else:
    sys.exit('Unknown widget type:  '+widget.get('type'))

# put the encoding line back at the top:
for line in minidom.parseString(ET.tostring(root)).toprettyxml(indent='  ',encoding='utf-8').decode('utf-8').split('\n'):
  if len(line.strip()) != 0:
    print(line)

