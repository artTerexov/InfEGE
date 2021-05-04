#  (А.М. Кабанов) В магазине сотовой связи представлены смартфоны различной стоимости.
#  Считается, что K самых дешёвых смартфонов относятся к бюджетному сегменту, а M
#  самых дорогих – к премиум сегменту. По заданной информации о цене каждого из смартфонов
#  определите цену самого дешёвого смартфона премиум сегмента, а также целую часть средней
#  цены телефона из бюджетного сегмента.
# Входные и выходные данные. В первой строке входного файла 26-k5.txt находятся три числа,
#  записанные через пробел: N – общее количество результатов учащихся (натуральное число,
# не превышающее 10 000), K – количество смартфонов в бюджетном сегменте, M – количество
#  смартфонов в премиум сегменте. В следующих N строках находятся значения каждого из
#  результатов (все числа натуральные, не превышающие 30000), каждое в отдельной строке.
# Запишите в ответе два числа: сначала цену самого дешёвого смартфона премиум сегмента,
#  а затем целую часть средней цены телефона из бюджетного сегмента.
# Пример входного файла:
# 10 3 2
# 28500
# 12000
# 17500
# 25000
# 18000
# 20000
# 22500
# 7500
# 19000
# 5500
# При таких исходных данных ответ должен содержать 2 числа – 25000 и 8333.
#  Пояснение: стоимость смартфонов из бюджетного сегмента: 5500, 7500, 12000;
#  стоимость смартфонов из премиум сегмента – 25000 и 28500. Минимальная цена премиум
#  смартфона 25000, а средняя цена бюджетного 8333,33.

f = open("26-k5.txt")
s = f.read().split()
f.close()

num = int(s[0])
numPoor = int(s[1])
numRich = int(s[2])

poorList = []
richList = []

priceList = [int(s[i]) for i in range(3, len(s))]
priceList.sort()

for i in range(0, numPoor):
    poorList.append(priceList[i])
for j in range(len(priceList) - 1, len(priceList) - numRich - 1, -1):
    richList.append(priceList[j])

print(min(richList), sum(poorList) // len(poorList))

# 27700 7896
