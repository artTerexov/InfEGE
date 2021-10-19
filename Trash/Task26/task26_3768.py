# В текстовом файле записан набор натуральных чисел. Гарантируется, что все числа различны. Рассматриваются пары чисел из набора, между которыми в отсортированном массиве помещаются не более 100 чисел из того же набора. Определите количество пар с суммой кратной 10, а также наименьшее среднее арифметическое таких пар.
# Входные данные представлены в файле 26-52.txt следующим образом. Первая строка содержит целое число N – общее количество чисел в наборе. Каждая из следующих N строк содержит одно число, не превышающее 109.
# В ответе запишите два целых числа: сначала количество пар, затем наименьшее среднее арифметическое.
# Пример входного файла:
# 8
# 3
# 8
# 14
# 11
# 2
# 16
# 5
# 9
# В примере рассмотрим пары, между которыми помещаются не более 3 чисел из набора. В данном случае есть три подходящие пары: 2 и 8, 9 и 11, 14 и 16. В ответе надо записать числа 3 и 5.

f = open("Files/26_3768.txt")
s = f.read().strip().split("\n")
f.close()

s.pop(0)

g = [int(i) for i in s]

g.sort()

buff = []

for i in range(0, len(g) - 1):
    for j in range(i + 1, len(g)):
        if j - i > 101:
            break
        summa = g[i] + g[j]
        if summa % 10 != 0:
            continue
        middle = (g[i] + g[j]) // 2
        buff.append(middle)

print(len(buff), min(buff))

# 49867 10002885

