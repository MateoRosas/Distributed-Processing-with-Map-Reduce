# -*- coding: utf-8 -*-
import sys

dict1={}
cont = 1
for line in sys.stdin:
   city = line.split("\t")
   value = int(city[1])
   #print(city[0], int(city[1]))
   if city[0] in dict1:
    dict1[city[0]] += value/cont
    cont += 1
   else:
    cont = 1
    dict1[city[0]] = value/cont
    
for key, values in dict1.iteritems():
   print '%s\t%s' % (key, values)
