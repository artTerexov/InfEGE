# Замкнутой цепочкой называется подстрока (часть одной строки файла) длиной не менее
# трёх символов, которая начинается и
# заканчивается на одну и ту же букву, но внутри этих букв не содержит.
# Нужно определите длину самой длинной замкнутой цепочки в строках, содержащих
# менее 30 букв R, а также общее количество замкнутых цепочек во всех таких строках.

# # # ABNJBNJDJBJDBAFDFDFDFDFDFDF
with open("files/4208.txt") as f:
    s = f.read().strip().split()

buffer = []
for i in s:
    if i.count("R") < 30:
        continue
    count = 1
    maximum = 0
    for j in range(len(i) - 1):
        startIndex = j
        try:
            endIndex = i.index(i[j], j + 1)
        except ValueError:
            continue
        maximum = max(maximum, endIndex - startIndex + 1)
    buffer.append(maximum)

print(max(buffer))





