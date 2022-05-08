with open('files/5135_A.txt') as f:
    s = [int(i) for i in f.readlines()][1:]

M = 345600
count = 0
k = [0] * M
prod = 1

for i in s:
    prod *= i
    if prod % M == 0:
