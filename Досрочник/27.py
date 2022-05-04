# Неэффективная
import time

start_time = time.time()
# with open('27_test') as f:
#     s = f.read().split()
#
# s = [int(i) for i in s]
# s.pop(0)
# print(*s)
# minCost = 1000000000000
# minNum = 0
# # Индекс завода
# for i in range(len(s)):
#     cost = 0
#     # Расстояние
#     for j in range(1, len(s) // 2 + 1):
#         if j == len(s) // 2 and len(s) % 2 == 0:
#             cost += s[i - j] * j
#         else:
#             cost += s[(i + j) % len(s)] * j + s[i - j] * j
#     if cost < minCost:
#         minCost = cost
#         minNum = i + 1
#
# print(minNum)
# print(minCost)


# Эффективная
with open('27-B.txt') as f:
    data = f.read().split()
data = [int(i) for i in data]
data.pop(0)
data1 = data * 2
dist = len(data) // 2
s = data[dist] * dist
# Считается сумма для первого элемента
for i in range(0, dist):
    s += data[0 + i] * i + data[0 - i] * i
res = [s]
summa = sum(data)
# Относительно первого с помощью префиксных сумм вычитаем на сколько изменяется следующее значение и добавляем его в список.
for i in range(len(data1) - 1):
    data1[i + 1] += data1[i]
for i in range(0, len(data)):
    res.append(res[i] + (data1[len(data) + i] - data1[i + len(data) // 2]) - (data1[i + len(data) // 2] - data1[i]))
# Выводим индекс минимальной суммы в списке + 1
print(res.index(min(res)) + 1)

print("--- %s seconds ---" % (time.time() - start_time))







