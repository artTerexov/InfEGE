# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# one two one tho three
# 0 0 1 0 0

# s = input()
# d = dict()
#
# for i in s.split():
#     if i in d:
#         print(d[i], end=" ")
#         d[i] += 1
#     else:
#         print(0, end=" ")
#         d[i] = 1

d = {"A": [1, 2, 3, 4, 5]}

print(d["B"])
print(d.get("B"))