#  В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
#  Рассматриваются всевозможные группы чисел, состоящие из любого количества элементов
#  последовательности. Необходимо найти наибольшую сумму такой группы, кратную 25. Программа должна вывести эту сумму.
# Входные данные. Даны два входных файла (файл A и файл B),
# каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000).
# Каждая из следующих N строк содержит одно натуральное число, не превышающее 10^8.
# Пример входного файла:
# 5
# 16
# 34
# 7
# 25
# 13
# Для указанных данных можно выбрать следующие группы: {16, 34}; {16, 34, 25}. Суммы элементов данных групп равны 50 и 75. Программа должна вывести наибольшую из этих сумм – 75.
# В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.

# Неэфективное решение на 1 балл

with open("files/27-60b.txt") as f:
    s = [int(i) for i in f.read().strip().split('\n')]
s.pop(0)
b = []
for i in s:
    b.append((i, i % 25))
b.sort()
print(b)
print(sum(s) - 41, (sum(s) - 41) % 25)

