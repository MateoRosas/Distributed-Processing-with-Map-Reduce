# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
busqueda = "LONDON"
busqueda_year ="1995"
count = 0
data_p = []
print(cabecera.strip().split(","))

def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return year

def findMoneyCity(name, year, money):
  if name == busqueda and year == busqueda_year:
    return name, year, int(money)


for line in sys.stdin:
  arreglo = line.strip().split(",")
  #print(arreglo[1], arreglo[2], arreglo[6])
  anne = manageYear(arreglo[2])
  if findMoneyCity(arreglo[6], anne, arreglo[1]) != None:
    data_p.append(findMoneyCity(arreglo[6], anne, arreglo[1]))

data_p.sort(key=lambda x: x[2], reverse = False)


for i in data_p:
  print(i)
