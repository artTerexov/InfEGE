# # 10 -> task16
# print(hex(11))
# # 10 -> 2
# print(bin(10))
# # x -> 10
# print(int("b", task16))

n = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1

a = str(hex(n))[2:]
print(a)
print(a.count("0"))

