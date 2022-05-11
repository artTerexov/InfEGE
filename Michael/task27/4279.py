with open('files/4279_A.txt') as f:
    s = [int(i) for i in f.readlines()[1:]]
print(s)
# Переборный алгоритм
buff = []
for i in range(len(s)):
    summa = s[i]
    if summa % 93 == 0 and summa % 2 != 0:
        buff.append(summa)
    for j in range(i + 1, len(s)):
        summa += s[j]
        if summa % 93 == 0 and summa % 2 != 0:
            buff.append(summa)

print(max(buff))