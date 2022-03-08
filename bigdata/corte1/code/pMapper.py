import sys

for line in sys.stdin:
    print(line.split(",")[6].replace(".", ""), ",", line.split(",")[1])
