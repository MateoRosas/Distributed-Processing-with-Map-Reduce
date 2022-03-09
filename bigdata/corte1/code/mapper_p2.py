# -*- coding: utf-8 -*-
import sys

cabecera = sys.stdin.readline()

for line in sys.stdin:
  arreglo = line.strip().split(",")
  print '%s\t%s\t%s' % (arreglo[6], arreglo[1], 1)
