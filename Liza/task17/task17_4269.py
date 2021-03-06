# В файле 4269.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от -10 000 до 10 000 включительно.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# в которых хотя бы одно число делится на 7, а другое при этом не делится на 17.
# Затем - минимальную из сумм элементов таких пар. В данной задаче под парой
# подразумевается два идущих подряд элемента последовательности. Например,
# для последовательности -45; 14; 22; -21; 34 ответом будет пара чисел: 3 и -31.


with open("files/4269.txt") as f:
    s = f.read().strip().split("\n")
s = [int(i) for i in s]

result = []
for i in range(len(s) - 1):
    num_1 = s[i]
    num_2 = s[i + 1]
    num_3 = s[i + 2]
    if (s[i] % 7 == 0 and s[i + 1] % 17 != 0) or (s[i] % 17 != 0 and s[i + 1] % 7 == 0):
        result.append(s[i] + s[i + 1])
    s.index()

print(len(result), min(result))
