# Выбиираем 3 числа(2, 4, 5) -> 2(10), 4(100), 5(101)
# if

with open("files/17-4361.txt") as f:
    s = [i for i in f.read().split()]

# a = []
# for i in s:
#     if len(i) == 3:
#         a.append(i)
#
# b = [[int(j) for j in i] for i in a]
#
# c = 0
# for i in b:
#     for j in i:
#         d = bin(j)