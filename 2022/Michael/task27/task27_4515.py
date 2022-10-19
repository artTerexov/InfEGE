# Дана последовательность натуральных чисел.
# Рассматриваются все её непрерывные подпоследовательности, в которых количество простых чисел кратно K = 9.
# Найдите наибольшую сумму такой подпоследовательности.


def isSimple(num):
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            return False
    return True


with open('files/27-82a.txt') as f:
    s = [int(i) for i in f.read().split()]
s.pop(0)

K = 9
summa = [10 ** 10] * K
summa[0] = 0
k = 0
m = 0
maxSum = 0

for i in s:
    k += i
    if isSimple(i):
        m += 1
    ostat = m % K
    if summa[ostat] == 10 ** 10:
        summa[ostat] = k
    if maxSum < k - summa[ostat]:
        maxSum = k - summa[ostat]

print(maxSum)