# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
#print(cabecera.strip().split(","))
dict1 = {}
count = 0
prom = 0
pricesPerCity = []

def lowestPrice(priceI, priceF):
 if priceF < priceI:
   return priceF
 else:
   priceI = priceF
   return priceI 

for line in sys.stdin:
  arreglo = line.strip().split(",")
  pricesPerCity = arreglo[1], arreglo[6]
  count = len(pricesPerCity) - 1
  initialValue = int(pricesPerCity[0])
  if pricesPerCity[1] in dict1:
    dict1[pricesPerCity[1]] = lowestPrice(int(pricesPerCity[0]), initialValue)
  else:
    dict1[pricesPerCity[1]] = int(pricesPerCity[0])

for key, values in dict1.iteritems():
  print(key, values)
