# def remake(num: int, base: int) -> str:
#     buff = ""
#     while num // base != 0:
#         buff += str(num % base)
#         num = num // base
#     buff += str(num)
#     return buff[::-1]
#
#
# n = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
# t = 6
#
# g = remake(n, t)
# print(g.count("5") - g.count("0"))
#
#
#
# # B = range(25, 41)
# #
# # C = range(12, 34)
