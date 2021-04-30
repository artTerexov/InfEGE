# В текстовом файле записан набор натуральных чисел. Гарантируется, что все числа различны. Рассматриваются пары с чётной суммой, такие что:
# - хотя бы половина чисел набора меньше среднего арифметического пары
# - хотя бы четверть чисел набора больше среднего арифметического пары
# Определите количество таких пар и наименьшее из средних арифметических таких пар.
# Входные данные представлены в файле 26-50.txt следующим образом. Первая строка содержит целое число N – общее количество чисел в наборе. Каждая из следующих N строк содержит одно число, не превышающее 109.
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
# В данном случае есть четыре подходящие пары: 2 и 16 (среднее арифметическое 9), 8 и 14 (среднее арифметическое 11), 9 и 11 (среднее арифметическое 10), 8 и 16 (среднее арифметическое 12). В ответе надо записать числа 4 и 9.

f = open('Files/26_3766.txt')
s = f.read()
f.close()

g = s.strip().split('\n')
g.pop(0)

sets = [int(i) for i in g]
sets.sort()

array = []
count = 0

middle = sets[len(sets) // 2 - 1]

quarter = sets[len(g) - (len(g) // 4)]

print(sets.index(middle), sets.index(quarter))

# 2351097 54751679

for i in range(0, len(sets) - 1):
    for j in range(i + 1, len(sets)):
        if (sets[i] + sets[j]) % 2 != 0:
            continue
        average = (sets[i] + sets[j]) // 2
        if middle <= average <= quarter:
            array.append(average)

print(len(array), min(array))
