import sys

cabecera = sys.stdin.readline()

for line in sys.stdin:
    print(line.split(",")[6], "\t",line.split(",")[8], "\t", 1)
