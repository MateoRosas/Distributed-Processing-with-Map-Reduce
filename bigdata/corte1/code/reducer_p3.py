import sys

current_word = None
current_value = 0
word = None
value = 0

for line in sys.stdin:
    word = line.split("\t")
    if(word[0] != "Town/City "):
       word[1] = int(word[1])
       if current_word == word[0]:
            if word[1] < current_value:
               current_value = word[1]
       else:
            if current_word:
               print('%s\t%s' % (current_word, current_value))
            current_word = word[0]
            current_value = word[1]

if current_word == word[0]:
    print('%s\t%s' % (current_word, current_value))
