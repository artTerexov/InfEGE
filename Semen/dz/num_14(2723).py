# В какой системе счисления выполняется равенство 12X · 31X = 402X?
# В ответе укажите число – основание системы счисления.

# import string
#
# def calc(x, y):
#     s = ""
#     while x > 0:
#         s += string.hexdigits[x % y]
#         x = x // y
#     return s[::-1]
#
#
# a, b = 12, 31
# for i in range(2, 18):
#     print(calc(a, i), calc(b, i), i)


for i in range(5, 16):
    if int('12', i) * int('31', i) == int('402', i):
        print(i)