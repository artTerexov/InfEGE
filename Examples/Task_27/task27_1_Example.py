# https://inf-ege.sdamgia.ru/problem?id=27424

f = open("Files/27_1_A.txt").read().split('\n')

minDiff = 100000
result = 0

for i in range(1, len(f) - 1):
    pair = f[i].split()
    numOne = int(pair[0])
    numTwo = int(pair[1])
    diff = abs(numOne - numTwo)
    result += max(numOne, numTwo)
    if minDiff > diff and diff % 3 != 0:
        minDiff = diff
if result % 3 == 0:
    print(result - minDiff)
else:
    print(result)