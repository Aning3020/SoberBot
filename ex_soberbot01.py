import random
lines = []
with open('ex_soberbot01.txt','r') as f:
    for line in f:
        lines.append(line.strip('\n').split(','))
#print(lines) # txt 装到 list 里
list_sentence = random.choice(lines) #随机返回一个句子，句子在list里
#print(list_sentence)
sentence = random.choice(list_sentence) #脱list
print(sentence)
