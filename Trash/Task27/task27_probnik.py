with open("Files/27_B.txt") as f:
    s = f.read().strip().split("\n")

s.pop(0)
summa = 0
buff = set()
for num in s:
    numBuff = [int(i) for i in num.split()]
    summa += max(numBuff)

    buff.add(max(numBuff) - min(numBuff))
    numBuff.pop(numBuff.index(min(numBuff)))
    buff.add(max(numBuff) - min(numBuff))

sorted(buff)

if summa % 101 == 0:
    for j in buff:
        if (summa - j) % 101 != 0:
            print(summa - j)
            break
else:
    print(summa)

# 7567616720
# 694390