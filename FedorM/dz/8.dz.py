# x = 0
# letters = "ПАНЕЛЬ"
# s = []
# for a in letters:
#     for b in letters:
#         for c in letters:
#             for d in letters:
#                 for e in letters:
#                     for k in letters:
#                         word = a + b + c + d + e + k
#                         if word.count('ЕАП') and a == 'Ь':
#                             break
#                         else:
#                             s.append(word)
#                             x += 1
# print(x)

import itertools

a = set(itertools.permutations("ПАНЕЛЬ", r=6))




