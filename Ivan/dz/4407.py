with open("4407.txt") as f:
    s = f.read().strip().split("\n")

buff = []
s = [int(i) for i in s]
for i in range(len(s) - 1):
    summa = s[i] + s[i + 1]
    if 99 < summa < 1000 and int(str(summa)[2]) > int(str(summa)[1]):
        buff.append(summa)

print(len(buff), min(buff))
