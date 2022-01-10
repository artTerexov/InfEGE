# В файле 4269.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество троек, в которых хотя бы два из трёх элементов больше,
# чем среднее арифметическое всех чисел в файле, и хотя бы один из трёх элементов делится на 11.
# В ответе запишите два числа: сначала количество найденных троек,
# а затем – максимальную сумму элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности


with open('4269.txt') as f:
    s = f.read().strip().split('\n')
s = [int(i) for i in s]
buff = []
average = sum(s) / len(s)
for i in range(0, len(s) - 2):
    a1 = 0
    a2 = 0
    for j in range(i, i + 3):
        if s[j] > average:
            a1 += 1
        if s[j] % 11 == 0:
            a2 += 1
    if a1 >= 2 and a2 >= 1:
        buff.append(s[i] + s[i + 1] + s[i + 2])
print(len(buff), max(buff))
