import sys

dict_city = {}
dict_county = {}
city = []
county = []
for line in sys.stdin:
   word = line.split("\t")
   #print(word)
   if word[0] in dict_county:
     county.append(word[0])
     dict_county[word[0]] += 1
     if word[1] in dict_city:
       city.append(word[0])
       dict_city[word[1]] += 1
     else:
       dict_city[word[1]] = 1
       city = []
   else:
      dict_county[word[0]] = 1
      county =[]
   #print(len(county), len(city))

for key, values in dict_county.iteritems():
   #print '%s' % (values)
   for key1, values1 in dict_city.iteritems():
      print '%s\t%s' % (values, values1)
