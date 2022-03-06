# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
#print(cabecera.strip().split(","))
dict1 = {}

def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return year, month

def highestPrice(priceI, priceF):
  if priceF > priceI:
    return priceF
  else:
    priceI = priceF
    return priceI


for line in sys.stdin:
  arreglo = line.strip().split(",")
  priceI = int(arreglo[1])
  data = manageYear(arreglo[2])
  #print(arreglo[1], manageYear(arreglo[2]))
  if data[1] in dict1:
   dict1[data[1]] = highestPrice(priceI, int(arreglo[1])), data[0]
  else:
   dict1[data[1]] = int(arreglo[1]), data[0]


for key, values in dict1.iteritems():
  print(key, values)
