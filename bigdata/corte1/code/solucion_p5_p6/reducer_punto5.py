import sys
from functools import reduce

date = None
value = 0
count_ = 0
max = 0
data = {}
mayor = 0
for line in sys.stdin:
   word, count, sum = line.split("\t")
   year, month = word.split("-")
   current_date = word
   current_value = int(sum)
   data[current_date] = 0
   if current_date in data:
     mayor += current_value
     data[current_date] = mayor
   else:
     mayor = 0
   

#dict(filter(lambda x: x[1] > 1, data.items()))
largest_num = reduce(lambda x, y: x if x>y else y, data.values())
print(largest_num)
