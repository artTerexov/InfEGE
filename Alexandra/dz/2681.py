# Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число
# так, чтобы сумма всех выбранных чисел оканчивалась на 8 и при этом была максимально возможной. Гарантируется, что
# искомую сумму получить можно. Программа должна напечатать одно число – максимально возможную сумму, соответствующую
# условиям задачи.

# with open('27-21a.txt') as f:
#     a = f.read().strip().split('\n')
#
# a.pop(0)
D = 10
# summa = 0
# dMin = [10000] * D
# for pair in a:
#     numOne = int(pair.split()[0])
#     numTwo = int(pair.split()[1])
#     summa += max(numOne, numTwo)
#     d = abs(numTwo - numOne)
#     r = d % D
#     if r > 0:
#         dMinNew = dMin.copy()
#         for k in range(1, D):
#             r0 = (r + k) % D
#             dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
#         dMinNew[r] = min(dMinNew[r], d)
#         dMin = dMinNew
#
# if summa % 10 == 8:
#     print(summa)
# else:
#     print(summa - dMin[(summa % 10) - 8])

with open('27-21b.txt') as f:
    b = f.read().strip().split('\n')

b.pop(0)
summa = 0
dMin = [10000] * D
for pair in b:
    numOne = int(pair.split()[0])
    numTwo = int(pair.split()[1])
    summa += max(numOne, numTwo)
    d = abs(numTwo - numOne)
    r = d % D
    if r > 0:
        dMinNew = dMin.copy()
        for k in range(1, D):
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
        dMinNew[r] = min(dMinNew[r], d)
        dMin = dMinNew

print(summa, summa % D)
print(dMin)
if summa % 10 == 8:
    print(summa)
else:
    print(summa - dMin[(summa % 10) - 8])
