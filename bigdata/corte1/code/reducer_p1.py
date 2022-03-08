# -*- coding: utf-8 -*-
import sys

dict1={}
for line in sys.stdin:
   year, n = line.split("\t", 1)
   if year in dict1:
    dict1[year] += 1
   else:
    dict1[year] = 1


   
for key, values in dict1.iteritems():
   print '%s\t%s' % (key, values)
