import sys

cabecera = sys.stdin.readline()


for line in sys.stdin:
    print '%s\t%s\t%s' % (line.split(",")[6], line.split(",")[8], 1)
