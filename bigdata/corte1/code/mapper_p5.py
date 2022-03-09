import sys

cabecera = sys.stdin.readline()

def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return int(year), int(month)


for line in sys.stdin:
    y, m = manageYear(line.split(",")[2])
    print '%s\t%s\t%s\t%s' % (y, m,  int(line.split(",")[1]), 1)
