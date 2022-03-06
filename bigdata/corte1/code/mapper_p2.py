# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
#print(cabecera.strip().split(","))
dict1 = {}
count = 0
prom = 0
pricesPerCity = []
for line in sys.stdin:
  arreglo = line.strip().split(",")
  pricesPerCity = arreglo[1], arreglo[6]
  #print(pricesPerCity)
  count = len(pricesPerCity) - 1
  if pricesPerCity[1] in dict1:
    prom += 1
    dict1[pricesPerCity[1]] += (int(pricesPerCity[0])/prom)
  else:
    dict1[pricesPerCity[1]] = int(pricesPerCity[0])
    
for key, values in dict1.iteritems():
  print(key, values)
