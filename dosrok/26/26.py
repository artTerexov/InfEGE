with open('26_7602.txt') as f:
    a = [[int(j) for j in i.split()] for i in f.readlines()]

a.sort()
limit = 210
buff = [0] * limit
count = 0
lastC = 0

for i in a:
    for j in range(len(buff)):
        if buff[j] == 0 or buff[j] < i[0]:
            buff[j] = i[1]
            count += 1
            lastC = j + 1
            break

print(count, lastC)