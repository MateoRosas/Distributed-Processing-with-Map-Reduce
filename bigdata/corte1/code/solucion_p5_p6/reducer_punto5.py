import sys
from functools import reduce

date = None
value = 0
count_ = 0
max = 0
data = {}
mayor = 0
current_word = None
current_value = 0

for line in sys.stdin:
   word, count, sum = line.split("\t")
   year, month = word.split("-")
   current_date = word
   #current_value = int(sum)
   if current_word == word:
      mayor += int(sum)
      data[current_word] = mayor
   else:
     mayor = 0
     current_word = word
     #current_value = int(sum)


for key, values in data.items():
    print(key, values)
