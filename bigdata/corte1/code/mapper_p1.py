# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
ountYear = []
dateTransfer =[]
dict1 = {}
def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return int(year)


for line in sys.stdin:
  arreglo = line.strip().split(",")
  dato = manageYear(arreglo[2])
  print '%s\t%s' % (dato, 1)
