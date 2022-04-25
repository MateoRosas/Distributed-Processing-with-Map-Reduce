import sys

max = 0
current_word = None
current_county = None
dict1 = {}
dict2 = {}
count_city = 0
count_county = 0
for line in sys.stdin:
    data= line.split("\t")
    city = data[0]
    county = data[1]

    if current_word == city:
      max += 1 
      dict2[current_word] = max
      if current_county == county and current_word in dict2.keys():
         count_county += 1
         dict1[max] = count_county
      else:
         count_county = 0
         current_county = county   
    else:
      count_city = 0
      current_word = city
    

for key, values in dict1.items():
   print(key, values)

