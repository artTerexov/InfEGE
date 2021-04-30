# Рассматривается множество целых чисел, принадлежащих числовому отрезку [5903; 174203],
# которые имеют все различные цифры, и при этом имеют в своей записи ровно три цифры большие 4.
# Найдите количество таких чисел и такое число наиболее близкое к 30000. В ответе запишите два целых числа:
# сначала количество, затем такое число наиболее близкое к 30000.


def different(number):
    array = []
    unique = []
    count = 0
    for j in str(number):
        array.append(j)
    for i in array:
        if i not in unique:
            unique.append(i)
        elif i in unique:
            break
        if int(i) > 4:
            count += 1
    if len(unique) == len(array) and count == 3:
        return 1
    else:
        return 0


array = [b for b in range(5903, 174204)]

bigCount = 0

buffer = []

for i in array:
    if different(i):
        bigCount += 1
        buffer.append(i)
buffer.append(30000)
buffer = sorted(buffer)
index = buffer.index(30000)
print(buffer[index - 1], buffer[index + 1])
print(bigCount)
