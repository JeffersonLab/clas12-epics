#!/usr/bin/env python3
import collections

columns = ['crate','slot','channel','sector','layer','component','order']
Translation = collections.namedtuple('Translation', columns)

class TranslationTable():
  def __init__(self, filename):
    self.table = []
    with open(filename,'r') as f:
      for line in f:
        if len(line.strip().split()) == 7:
          self.table.append(Translation(*[int(x) for x in line.strip().split()]))
  def __iter__(self):
    self.n = 0
    return self
  def __next__(self):
    if self.n < len(self.table):
      self.n += 1
      return self.table[self.n-1]
    else:
      raise StopIteration

translation_table = iter(TranslationTable('ctof-v1290.txt'))

with open('jscalers_CTOF_DISC.substitutions','r') as f:
  for line in f:
    if line.strip().startswith('{'):
      t = next(translation_table)
      line = line.replace('""', '"%s%.2d"' % ( ['U','D'][t.order-2] , t.component ) )
    print(line.strip())

#with open('jscalers_CTOF_DISC.substitutions','r') as f:
#  pv_index = 0
#  for line in f:
#    if line.strip().startswith('{'):
#      line = line.replace('""','"%s%.2d"'%(['U','D'][pv_index%2],pv_index/2+1))
#      pv_index += 1
#    print(line.strip())

