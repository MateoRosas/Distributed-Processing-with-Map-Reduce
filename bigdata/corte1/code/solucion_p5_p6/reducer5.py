import sys

current_year = None
current_count = 0
word = None
count = 0
mount = None
max = 0
year = None
sum_1 = 0
dict1 = {}

for line in sys.stdin:
   word, count, sum = line.split("\t")
   year, month = word.split("-")

   count = int(count[1])
   sum = int(sum)
   #print(year, month, sum, count)
   dict1[word] = sum
   if word in dict1:
     sum_1 += sum
     dict1[word] = sum_1


#dict(sorted(dict1.items(), key=lambda item: item[1]))
#d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(dict1.items(), key=lambda x: x[1], reverse=True)    

for i in a:
   print(i[0], i[1])
