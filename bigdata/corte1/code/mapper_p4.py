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
