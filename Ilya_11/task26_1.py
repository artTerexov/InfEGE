# Системный администратор раз в неделю создаёт архив пользовательских файлов.
# Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный
# объём архивируемых файлов. Известно, какой объём занимает файл каждого пользователя.
# По заданной информации об объёме файлов пользователей и свободном объёме на архивном
# диске определите максимальное число пользователей, чьи файлы можно сохранить в
# архиве, а также максимальный размер имеющегося файла, который может быть сохранён
# в архиве, при условии, что сохранены файлы максимально возможного числа пользователей.
# Входные данные. В первой строке входного файла 26.txt находятся два числа:
# S – размер свободного места на диске (натуральное число, не превышающее 100 000) и
# N – количество пользователей (натуральное число, не превышающее 10 000). В
# следующих N строках находятся значения объёмов файлов каждого пользователя
# (все числа натуральные, не превышающие 100), каждое в отдельной строке.
# Запишите в ответе два числа: сначала наибольшее число пользователей, чьи
# файлы могут быть помещены в архив, затем максимальный размер имеющегося файла,
# который может быть сохранён в архиве, при условии, что сохранены файлы
# максимально возможного числа пользователей.
# Пример входного файла:
# 100 4
# 80
# 30
# 50
# 40
# При таких исходных данных можно сохранить файлы максимум двух пользователей. Возможные объёмы этих двух файлов 30 и 40, 30 и 50 или 40 и 50. Наибольший объём файла из перечисленных пар – 50, поэтому ответ для приведённого примера: 2 50

with open("26.txt", "r") as f:
    s = f.read().strip().split("\n")
size = int(s[0].split()[0])
s.pop(0)
g = [int(i) for i in s]
g.sort()
summa = []

for i in g:
    if sum(summa) + i <= size:
        summa.append(i)

summa.pop(-1)
diff = size - sum(summa)
for i in range(diff, 0, -1):
    if i in g:
        summa.append(i)
        break
print(len(summa), max(summa))
