# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()

dic_county = {}
dic_city = {}
dic_prueba = {}

#print(cabecera.strip().split(","))
for line in sys.stdin:
  arreglo = line.strip().split(",")
  #print(arreglo[6], arreglo[8])
  if arreglo[6] in dic_county:
    dic_county[arreglo[6]] += 1
    if arreglo[8] in dic_city:
      dic_city[arreglo[8]] += 1
    else:
      dic_city[arreglo[8]] = 1
    dic_prueba[arreglo[6]] = dic_city.values()
  else:
    dic_county[arreglo[6]] = 1
    #dic_prueba[arreglo[6]] = dic_city.values(), dic_city.keys()
  
for key, values in dic_prueba.iteritems():
  print(key, values)
