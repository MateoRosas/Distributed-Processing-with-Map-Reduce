import sys

current_word = None
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
   dict1[word] = sum
   if word in dict1:
     sum_1 += sum
     dict1[word] = sum_1

dict2 = {}
mayor = 0
name = None
for key, value in dict1.items():
   count += 1
   if current_word == key:
     current_count += count
   else:
     if current_word:
       if max < current_count:
         name = current_word
         max = current_count
         mayor = value
       if(current_word[5:-1] == "12" or current_word == "2017-05 "):
         print(name, mayor, "1")         
     current_word = key
     current_count = count

#for key, value in dict2.items():
#   print(key, value, count)

if current_word == word:
  print(current_word, mayor, "1")
