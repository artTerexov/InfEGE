# https://inf-ege.sdamgia.ru/problem?id=27891

f = open("Files/27_2_A.txt").read().split()

maxElement = -1
maxIndex = -1

maxMultiple = -1

for i in range(1, len(f)):
    num = int(f[i])

    if maxElement < num:
        maxElement = num
        maxIndex = i
    if num % 14 == 0 and i != maxIndex and num > maxMultiple:
        maxMultiple = num
print(maxMultiple * maxElement)
