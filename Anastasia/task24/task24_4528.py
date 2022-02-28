# (№ 4528) Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек,
# всего не более 106 символов. Определите максимальное количество идущих подряд символов,
# среди которых не более пяти точек.


# with open('files/4528.txt') as f:
#     s = f.read().split('.')
#
# point = 0
# count = 0
# count_max = 0
#
# for i in s:
#     if i == '.' and count == 0:
#         continue
#     count += 1
#     if i == '.':
#         point += 1
#     if point == 6:
#         if count > count_max:
#             count_max = count - 1
#         count = 0
#         point = 0
#
# print(count_max)

s = "ABC.....DVDFVDFSB.....ABCCDFAF"
s = s.split('.')
print(s)


# ABC.....DVDFVDFSB.....ABCCDFAF
# 17
# 22