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

def maxN(max, sum):
  if max < sum:
    max = sum
    return max
  else:
    return sum


for line in sys.stdin:
   word, count, sum = line.split("\t")
   year, month = word.split("-")

   count = int(count[1])
   sum = int(sum)
   #print(year, month, sum, count)
   dict1[word] = maxN(max, sum)
   if word in dict1:
     dict1[word] = maxN(max, sum)
     #dict1[word] = sum
     #print(dict1[word], sum)

for key, values in dict1.items():
  print(key,values,count)

