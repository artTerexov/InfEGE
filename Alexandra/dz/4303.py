# (№ 4303) (А. Кабанов) В файле 17-3.txt содержится последовательность целых чисел. Элементы последовательности могут
# принимать целые значения от -10 000 до 10 000 включительно. Определите и запишите в ответе сначала количество пар
# элементов последовательности, в которых произведение нечётно, а среднее арифметическое делится на 7, затем минимальное
# из средних арифметических элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента
# последовательности.
a = []
with open('17-3.txt') as f:
    a = [int(i) for i in f]

b = []
for i in range(len(a) - 1):
    if (a[i] * a[i + 1]) % 2 != 0 and ((a[i] + a[i + 1]) / 2) % 7 == 0:
        b.append((a[i] + a[i + 1]) / 2)
print(len(b), int(min(b)))