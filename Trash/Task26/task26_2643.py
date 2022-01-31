# Робот складывает монеты в ящики. Задача робота заполнить как можно большее количество ящиков
# монетами в количестве 100 штук. Роботу по конвейеру поступают корзины с монетами. В каждой
# корзине может быть от 1 до 99 монет. Известно, что робот может высыпать в ящик содержимое не
# более двух корзин. Необходимо определить, сколько ящиков можно заполнить монетами по 100.
# Входные данные представлены в файле task26-j1.txt следующим образом. В первой строке записано
# число N – количество корзин, в каждой из последующих N строк число K – количество монет в
# каждой корзине.
# В качестве ответа дать одно число – количество ящиков, заполненными 100 монетами.
# Пример входного файла:
# 7
# 10
# 44
# 66
# 90
# 65
# 47
# 34
#
# При таких исходных данных можно заполнить только 2 ящика по 100 монет 10 + 90 и 66 + 34.

with open('Files/26_2643.txt') as f:
    s = f.read().strip()


array = [int(number) for number in s.split('\n')]
num_size = array[0]
array.pop(0)
final = []

for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if array[i] + array[j] == 100:
            final.append([array[i], array[j]])
            array.pop(j)
            break
print(len(final))

# f = open("Files/26_2643.txt")
# s = f.read().strip().split("\n")
# f.close()
#
# s.pop(0)
#
# # g = []
# #
# # for i in s:
# #     g.append(int(i))
#
# g = [int(i) for i in s]
# count = 0
#
# newList = g[::]
#
# for i in range(0, len(g)):
#     diff = 100 - g[i]
#     if diff in newList:
#         count += 1
#         try:
#             newList.pop(newList.index(g[i]))
#             newList.pop(newList.index(diff))
#         except Exception:
#             count -= 1
#             continue
#
# print(count)