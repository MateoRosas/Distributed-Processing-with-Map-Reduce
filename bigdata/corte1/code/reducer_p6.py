# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()

dic_county = {}
dic_city = {}
dic_prueba = {}

print(cabecera.strip().split(","))
for line in sys.stdin:
  arreglo = line.strip().split(",")
  #print(arreglo[6], arreglo[8])
  if arreglo[6] in dic_county:
    dic_county[arreglo[6]] += 1
    dic_prueba[arreglo[6]] += " , "+arreglo[8]
  else:
    dic_county[arreglo[6]] = 1
    dic_prueba[arreglo[6]] = arreglo[8]
  
  if arreglo[8] in dic_city:
    dic_city[arreglo[8]] += 1
  else:
    dic_city[arreglo[8]] = 1

#print("Diccionario de condados**********************\n")
for i in dic_county:
  frecuency = dic_county[i]
  #print(i, frecuency)
  #print("\n")

#print("Diccionario de ciudades*********************\n")
for i in dic_city:
  frecuency = dic_city[i]
  #print(i, frecuency)
  #print("\n")


#print("Diccionario de pruebas*********************\n")
for i in dic_prueba:
  #frecuency = dic_prueba[i]
  print(i, frecuency)
  #print("\n")
