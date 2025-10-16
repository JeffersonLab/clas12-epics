#!/usr/bin/env python3
import collections

header = collections.OrderedDict()
header['Cr'] = 2
header['CrName'] = 8
header['CrType'] = 6
header['Sl'] = 2
header['Ch'] = 2
header['Sys'] = 5
header['Det'] = 5
header['Element'] = 7
header['CScode'] = 7
header['pwonoff'] = 7
header['v0set'] = 7
header['i0set'] = 7
header['trip'] = 7
header['rampup'] = 7
header['rampdn'] = 7
header['svmax'] = 7
header['enable'] = 7

commands = collections.OrderedDict()
commands['pwonoff'] = 0x0B
commands['v0set'] = 0x02
commands['i0set'] = 0x05
commands['trip'] = 0x0A
commands['rampup'] = 0x04
commands['rampdn'] = 0x03
commands['svmax'] = 0x0D
commands['enable'] = 0x01

def reader():
    for line in open('prad.txt','r').readlines():
        cols = line.strip().split()
        if not line.startswith('#') and len(cols) > 2:
            d = collections.OrderedDict()
            crate = int(cols[0][-1])
            slot = int(cols[1])
            channel = int(cols[2])
            d['CrName'] = 'PRIMEXHV'+cols[0][-1]
            d['CrType'] = '1527'
            d['Sys'] = 'HV'
            d['Det'] = 'HYCAL'
            d['Cr'] = '%0.2d'%crate
            d['Sl'] = '%0.2d'%slot
            d['Ch'] = '%0.2d'%channel
            d['Element'] = cols[3]
            d['CScode'] = '#C0x%x' % (crate + (slot<<8))
            channel = int(cols[2])
            for c in commands.keys():
                d[c] = 'S0x%x' %(channel+256*commands[c])
            d['CrId'] = crate
            yield d

def format_row(values, quotes):
    if quotes: values = [ '"%s"' % x for x in values ]
    else:      values = [ '%s' % x for x in values ]
    fmt = ', '.join([ '%%%ds' % (x+2) for x in header.values() ])
    return '{ ' + fmt % tuple(values) + ' }'

def mainframe(i):
    s = ['file "db/caenhv.db" {']
    s.append('pattern ' + format_row(tuple(header.keys()),False))
    for d in reader():
        if ( d['CrId'] & 0xff ) == i:
            v = [ d.get(h) for h in header.keys() if h != 'CrId' ]
            s.append('        ' +format_row(tuple(v),True))
    s.append('}')
    return s

import sys
for i in range(1,6):
    with open('PRIMEXHV%d.substitutions'%i,'w') as f:
        f.write('\n'.join(mainframe(i)))


