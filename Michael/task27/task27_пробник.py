with open('files/27_B (3).txt') as f:
    s = [int(i) for i in f.read().split()]
s.pop(0)

summa = [10 ** 10] * 67
k = 0
maxSum = 0

for i in s:
    k += i
    ostat = k % 67
    if summa[ostat] == 10 ** 10:
        summa[ostat] = k
    if maxSum < k - summa[ostat]:
        maxSum = k - summa[ostat]

print(maxSum)
