# -*- coding: utf-8 -*-
import sys

dict1={}
num = []

alfa = 0

for line in sys.stdin:
   city = line.split("\t")
   value = int(city[1])
   #print(city[0], int(city[1]))
   
   if city[0] in dict1:
    num.append(value)
    #alfa += value
    #print(alfa, len(num), alfa/len(num))
    dict1[city[0]] += float(value/len(num))
    
   else:
    dict1[city[0]] = float(value)
    num = []
    
for key, values in dict1.iteritems():
   print '%s\t%s' % (key, values)
