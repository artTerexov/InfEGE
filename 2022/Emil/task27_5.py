
with open('27-25a.txt') as f:
    s = f.read().strip().split('\n')


s.pop(0)
summa = 0

dMin = [100001] * 8

for i in s:
    first, second = map(int, i.split())
    mini = max(first, second)
    summa += mini
    raznost = abs(first - second)
    r = raznost % 8

if summa % 8 != 3:
    for j in n:
        if (summa - j) % 8 == 3:
            print(summa - j)
            break
else:
    print(summa)
