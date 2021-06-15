#  (Демовариант 2021 г.). Имеется набор данных, состоящий из пар положительных целых чисел.
#  Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел
#  не делилась на 3 и при этом была максимально возможной. Гарантируется, что искомую сумму
#  получить можно. Программа должна напечатать одно число – максимально возможную сумму,
#  соответствующую условиям задачи.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в
# первой строке количество пар N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит
# два натуральных числа, не превышающих 10 000.
# Пример входного файла:
# 6
# 1 3
# 5 12
# 6 9
# 5 4
# 3 3
# 1 1
# Для указанных входных данных значением искомой суммы должно быть число 32.
# В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.

with open("27-b.txt") as f:
    s = f.read().strip().split("\n")

s.pop(0)

summa = 0
d = []
for i in s:
    numOne = int(i.split()[0])
    numTwo = int(i.split()[1])
    summa += max(numOne, numTwo)
    d.append(abs(numOne - numTwo))

d.sort()

if summa % 3 == 0:
    for j in d:
        if (summa - j) % 3 != 0:
            print(summa - j)
            break
else:
    print(summa)


