import sys

cabecera = sys.stdin.readline()
#busqueda = "STAMFORD"
#busqueda_year ="2015"

busqueda = "STAMFORD"
busqueda_year = "2015"


def manageYear(date):
  date_s, hour = date.strip().split(" ")
  year, month, day = date_s.strip().split("-")
  return year

def findMoneyCity(name, year, money):
  if name == busqueda and year == busqueda_year:
    return name, int(year), int(money)
  else:
    return None, None, None

for line in sys.stdin:
  arreglo = line.strip().split(",")
  anne = manageYear(arreglo[2])
  #print("{}\t{}\t{}" .format(findMoneyCity(arreglo[6], anne, arreglo[1])))
  #print '%s\t%s\t%s\t%s' % (findMoneyCity(arreglo[6], anne, arreglo[1]))
  n, y, m  = findMoneyCity(arreglo[6], anne, arreglo[1]) 
  print '%s\t%s\t%s\t%s' % (n, y, m, 1)
