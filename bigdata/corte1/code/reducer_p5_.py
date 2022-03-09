import sys

current_year = None
current_month = None
current_price = 0
count_price = 0
dict1 = {}
num = []

def highestPrice(priceI, priceF, month):
 if priceF > priceI:
  priceI = priceF
  return month
 else:
  return month
 

for line in sys.stdin:
    word = line.split("\t")
    current_year = word[0]
    current_month = word[1]
    #current_price = int(word[2])
    #print(year, month, price)
    if current_year in dict1:
       count_price +=current_price
       m  = highestPrice(current_price, int(word[2]), current_month)
       dict1[current_year] = (m, count_price)
    else:
      dict1[current_year] = word[1]
      current_price = int(word[2])
      current_month = word[1]
      count_price = 0

for key, values in dict1.iteritems():
  print '%s\t%s\t%s'%(key, values, 1)

#print(dict1)
