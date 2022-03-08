# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()
dict1 = {}
cont = 1
for line in sys.stdin:
    word = line.strip().split(",")
    #print(word[1])
    if word[0] in dict1:
      dict1[word[0]] += 1
    else:
      dict1[word[0]] = 1

for key, value in dict1.iteritems():
  print(key, value)
      
    
