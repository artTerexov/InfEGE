with open('9.txt') as f:
    s = f.readlines()

count = 0

for i in s:
    el = [int(j) for j in i.split('\t')]
    el.sort()
    if (el[-1] + el[0]) ** 2 > (el[1] ** 2 + el[2] ** 2 + el[3] ** 2):
        count += 1
print(count)