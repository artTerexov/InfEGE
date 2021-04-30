# Имеется набор данных, состоящий из пар положительных целых чисел.
# Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма
# всех выбранных чисел в шестнадцатеричной системе счисления оканчивалась на
# F и при этом была минимально возможной. Гарантируется, что искомую сумму
# получить можно. Программа должна напечатать одно число – минимально возможную
# сумму, соответствующую условиям задачи.

# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых
# содержит в первой строке количество пар N (1 ≤ N ≤ 100000). Каждая из следующих
# N строк содержит два натуральных числа, не превышающих 10 000.
# Пример входного файла:
# 6
# 3 5
# 5 12
# 6 9
# 5 4
# 7 9
# 5 1
# Для указанных входных данных значением искомой суммы должно быть число 31, которое в
# шестнадцатеричной системе счисления записывается как 1F16.
# В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.

f = open("27-26b.txt")
a = f.read().strip()
f.close()

generator = [i for i in a.split("\n")]

pairNum = int(generator[0])
generator.pop(0)

D = 16

summa = 0

dMin = [100001] * D

for pair in generator:
    numOne = int(pair.split()[0])
    numTwo = int(pair.split()[1])
    summa += min(numOne, numTwo)
    d = abs(numTwo - numOne)
    r = d % D
    if r > 0:
        dMinNew = dMin
        for k in range(1, D):
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
        dMinNew[r] = min(d, dMinNew[r])
        dMin = dMinNew
if summa % 16 == 15:
    print(summa)
else:
    print(summa + dMin[15 - (summa % 16)])















# for pair in generator:
#     numOne = int(pair.split()[0])
#     numTwo = int(pair.split()[1])
#     summa += min(numOne, numTwo)
#     d = abs(numTwo - numOne)
#     r = d % D
#     if r > 0:
#         dMinNew = dMin
#         for k in range(1, D):
#             r0 = (r + k) % D
#             dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
#         dMinNew[r] = min(d, dMinNew[r])
#         dMin = dMinNew
# if summa % D == 15:
#     print(summa)
# else:
#     print(summa + dMin[15 - (summa % D)])
#
# print(633 % 16)
