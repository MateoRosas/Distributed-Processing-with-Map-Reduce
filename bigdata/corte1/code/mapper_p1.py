# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
#print(cabecera.strip().split(","))
countYear = []
dateTransfer =[]
years_s = [str(i) for i in range(1994, 2018, 1)]
dict1 = {}
def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return year


for line in sys.stdin:
  arreglo = line.strip().split(",")
  countYear.append(manageYear(arreglo[2]))
  counter = len(countYear) - 1
  if countYear[counter] in dict1: 
    dict1[countYear[counter]] += 1
  else:
    dict1[countYear[counter]] = 1
  
for key, values in dict1.iteritems():
  print(key, values)


