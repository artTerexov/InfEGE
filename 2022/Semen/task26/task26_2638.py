with open('files/2638.txt') as f:
    s = f.read().strip().split()

tovarNum = int(s[0])
saleNum = int(s[1])
tovars = [int(s[i]) for i in range(2, len(s))]
summa = 0
tovars.sort(reverse=True)

for j in range(saleNum):
    summa += tovars[j] * 0.2

print(tovars[saleNum], summa)