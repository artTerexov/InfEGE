# В файле 17-1.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество троек, в которых хотя бы два из трёх элементов меньше, чем среднее арифметическое всех чисел
# в файле, и десятичная запись хотя бы двух из трёх элементов оканчивается на 8. В ответе запишите два числа:
# сначала количество найденных троек, а затем – максимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

# with open("17.txt") as f:
#     s = [int(i) for i in f.read().strip().split()]
#
# h = sum(s) / len(s)
#
# a = []
#
# for i in range(len(s) - 2):
#     suma = 0
#     count = 0
#     count1 = 0
#     for j in range(i, i + 3):
#         # исправил
#         suma += s[j]
#         if s[j] < h:
#             count += 1
#         if str(s[j])[-1] == "8":
#             print("bad=", s[j], end=" ")
#             count1 += 1
#         if s[j] % 10 == 8:
#             print("norm=", s[j])
#
#     if count >= 2 and count1 >= 2:
#         a.append(suma)
#
# print(len(a), max(a))

# 159 4697

# cr_znach = sum(a) // len(a)
#
#
# def check(a, b, c):
#     count = 0
#     count_1 = 0
#     if a < cr_znach:
#         count += 1
#     if b < cr_znach:
#         count += 1
#     if c < cr_znach:
#         count += 1
#     if a % 10 == 8:
#         count_1 += 1
#     if b % 10 == 8:
#         count_1 += 1
#     if c % 10 == 8:
#         count_1 += 1
#     if count >= 2 and count_1 >= 2:
#         return 1
#
#
# b = []
# for i in range(len(a) - 2):
#     if check(a[i], a[i + 1], a[i + 2]) == 1:
#         b.append(a[i] + a[i + 1] + a[i + 2])
# print(len(b), max(b))