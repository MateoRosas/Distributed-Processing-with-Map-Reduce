import sys

data_p = []
menor = 0

for line in sys.stdin:
  arreglo = line.strip().split("\t")
  if arreglo[0] != "None":
    
    alfa = str(arreglo[0]),arreglo[2],str(arreglo[1])
    data_p.append(alfa)

data_p.sort(key=lambda x: x[1], reverse = False)
for i in data_p:
  print '%s\t%s\t%s' % (i[0], i[1], i[2])
