import string

num = 3*11**58 + 15*11**55 - 99*11**18 + 125*11**9 + 381
base = 11

# 1-способ поиска уникальных(различных) цифр
# result = set()
#
# while num > 0:
#     result.add(str(num % base))
#     num = num // base
# print(len(result))

# 2-способ поиска уникальных(различных) цифр
result = ''
d = '0123456789abcdefghijklmnopqrstuvwxyz'

while num > 0:
    result = d[num % base] + result
    num = num // base
print(result)