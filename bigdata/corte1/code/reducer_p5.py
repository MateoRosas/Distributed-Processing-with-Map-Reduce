import sys

current_word = None
current_count = 0
word = None
count = 0
mount = None
max = 0
year = None
price = 0

for line in sys.stdin:
    word = line.split("\t")
    #print(word[0], word[1][0])
    if(word != "Date of "):
        count = int(word[1][0])
        year = word[0]
        price = int(word[2])
        if current_word == word[0]:
            current_count += count
            current_price += price
        else:
            if current_word:

                if(max < current_count):
                    mount = current_word
                    max = current_count
                    price = current_price
                if(current_word[5:7] == "12" or current_word == "2017-05 "):
                    print "%s\t%s\t%s\t%s"% (mount, max, price, 1)
                    max = 0
                    price = 0

            current_count = count
            current_word = word[0]
            current_price = int(word[2])

if current_word == word[0]:
    print('%s\t%s\t%s\t%s' % (current_word, current_count, current_price, 1))
