# Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает
# 1000. Требуется найти для этой последовательности контрольное значение – наибольшее число R,
# удовлетворяющее следующим условиям:
# – R – произведение двух различных переданных элементов последовательности («различные» означает,
# что не рассматриваются квадраты переданных чисел, произведения различных, но равных по величине
# элементов допускаются);
# – R делится на 6.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой
# строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное
# число, не превышающее 10 000.
# Пример входного файла:
# 6
# 60
# 17
# 3
# 7
# 9
# 60
# Для указанных входных данных искомое контрольное значение равно 3600.
# В ответе укажите два числа: сначала контрольное значение для файла А, затем для файла B.


# 2 и 3. 6

with open("files/27-6b.txt") as f:
    s = f.read().strip().split()

s = [int(s[i]) for i in range(1, len(s))]

maximum = 0

div_3 = []
div_2 = []
div_6 = []
div_other = []

for i in range(len(s)):
    if s[i] % 2 == 0 and s[i] % 6 != 0 and s[i] % 3 != 0:
        div_2.append(s[i])
    elif s[i] % 3 == 0 and s[i] % 6 != 0 and s[i] % 2 != 0:
        div_3.append(s[i])
    elif s[i] % 6 == 0:
        div_6.append(s[i])
    else:
        div_other.append(s[i])

print(max(max(div_2) * max(div_3), max(div_6) * max(div_other)))

# for i in range(len(s) - 1):
#     for j in range(i + 1, len(s)):
#         R = s[i] * s[j]
#         if R % 6 == 0:
#             maximum = max(maximum, R)

print(maximum)
