import sys

cabecera = sys.stdin.readline()
for line in sys.stdin:    
  print(line.split(",")[2][0:7] ,"\t",1, "\t", line.split(",")[1])
