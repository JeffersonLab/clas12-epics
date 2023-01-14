#!/usr/bin/env python3
import sys,math,argparse

ANAPOWER=16.60

# C = Moeller L/R coincidences
# A = Moeller L/R accidentals
# S = SLM

def analyze(filename,args):
  CP,CM,AP,AM,SP,SM,ROW=0,0,0,0,0,0,0
  for xx in open(filename,'r').readlines():
    if xx.find('a')>=0:
      continue
    columns=xx.strip().split()
    if len(columns)!=6:
      print('Invalid Data:')
      sys.exit(columns)
    cp,cm,ap,am,sp,sm=columns
    CP += float(cp)
    CM += float(cm)
    AP += float(ap)
    AM += float(am)
    SP += float(sp)
    SM += float(sm)
    ROW += 1
    if args.nmax>0 and ROW>args.nmax:
      break

  MP = CP-AP
  MM = CM-AM

  if args.nobca:
    NUMERATOR   = MP - MM
    DENOMINATOR = MP + MM
    ASY = NUMERATOR / DENOMINATOR
    EASY = 0 # FIXME

  else:
    NUMERATOR   = SM*MP - SP*MM
    DENOMINATOR = SM*MP + SP*MM
    ASY = NUMERATOR / DENOMINATOR
    EASY_A = SM * (1-ASY)*(1-ASY) * ( (CP-AP)*(CP-AP) + SM*(CP+AP) )
    EASY_B = SP * (1+ASY)*(1+ASY) * ( (CM-AM)*(CM-AM) + SP*(CM+AM) )
    EASY = math.sqrt( (EASY_A+EASY_B) / DENOMINATOR / DENOMINATOR )

  POL  = 100 * ANAPOWER * ASY
  EPOL = 100 * ANAPOWER * EASY

  print(filename+'::::   '+'ASY: %.5f +/- %.5f     POL: %.5f +/- %.5f  '%(ASY,EASY,POL,EPOL))

#########################################################################
#########################################################################

cli = argparse.ArgumentParser(description='Analyze Moeller Run Data')
cli.add_argument('--nobca',help='disable beam charge asymmetry correction',default=False,action='store_true')
cli.add_argument('--nmax',help='max number of readings to include',default=-1,type=int)
cli.add_argument('filename',help='path to data file to analyze',nargs='+')

args = cli.parse_args(sys.argv[1:])

for x in args.filename:
  try:
    analyze(x,args)
  except ZeroDivisionError:
    pass

