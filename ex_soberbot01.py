import random
lines = []
with open('ex_soberbot01.txt','r') as f:
    for line in f:
        lines.append(list(line.strip('\n').split(',')))
print(random.choice(lines))
