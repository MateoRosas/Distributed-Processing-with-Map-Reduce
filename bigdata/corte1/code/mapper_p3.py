import sys

cabecera = sys.stdin.readline()


for line in sys.stdin:
    #print(line.split(",")[6].replace(".", ""), ",", line.split(",")[1])
    num = int(line.split(",")[1])
    #print(line.split(",")[6], num)
    print '%s\t%s\t%s' % (line.split(",")[6], num, 1)
