# (№ 4681) В файле 17-1.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество троек, в которых хотя бы два из трёх элементов больше, чем среднее
# арифметическое всех чисел в файле, и хотя бы один из трёх элементов делится на 11.
# В ответе запишите два числа: сначала количество найденных троек, а затем –
# максимальную сумму элементов таких троек. В данной задаче под тройкой подразумевается
# три идущих подряд элемента последовательности


with open("files/17-1.txt") as f:
    s = f.read().strip().split("\n")
a = []
s = [int(i) for i in s]
average = sum(s) / len(s)

for i in range(len(s) - 2):
    count_1 = 0
    count_2 = 0
    for j in range(i, i + 3):
        if s[j] > average:
            count_1 += 1
        if s[j] % 11 == 0:
            count_2 += 1
    if count_1 >= 2 and count_2 >= 1:
        a.append(s[i] + s[i + 1] + s[i + 2])
print(len(a), max(a))

