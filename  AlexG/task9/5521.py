with open('5521') as f:
    s = [[int(j) for j in i.split()]for i in f.readlines()]


for i in s:
    k = set(i)
    if len(k) == 5:
        print('OK')