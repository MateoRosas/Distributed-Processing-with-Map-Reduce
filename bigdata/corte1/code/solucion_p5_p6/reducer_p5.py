import sys

current_word = None
current_count = 0
word = None
count = 0
mount = None
max = 0
year = None
sum_1 = 0


for line in sys.stdin:
    word, count, sum = line.split("\t")
#    print(word, count, sum)
    if(word != "Date of "):
        count = int(count[1])
        year = word
        sum_1 = int(sum)
        if current_word == word:
            current_count += count
        else:
            if current_word:
                if(max < current_count):
                    mount = current_word
                    max = current_count
                    sum_1 += int(sum)
                if(current_word[5:7] == "12" or current_word == "2017-05 "):
                    print(mount, "\t", max ,"\t", sum_1)
                    max = 0
            sum_1 = 0
            current_count = count
            current_word = word

if current_word == word:
    print('%s\t%s\t%s' % (current_word, current_count, sum_1))
