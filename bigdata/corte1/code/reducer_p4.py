import sys

data_p = []
menor = 0

for line in sys.stdin:
  arreglo = line.strip().split("\t")
  if arreglo[0] != "None":
    
    data_p = [str(arreglo[0]),arreglo[2],str(arreglo[1])]
    #print(data_p)
    data_p.sort(key=lambda x: x[1], reverse = False)
    print '%s\t%s\t%s' % (data_p[0], data_p[1], data_p[2])
