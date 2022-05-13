# (№ 4619) Значение выражения 11•1565 + 18•1538 – 14•1517 + 19•1511 + 18338
# записали в системе счисления с основанием 15. Сколько различных цифр содержится в этой записи?


a = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
base = 15
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
s = ''

while a > 0:
    s += str(l[a % base])
    a //= base

print(s[::-1])

result = [s.count(str(i)) for i in l]
result = {i for i in s}
print(len(result))
print(result)

# B000000000000000000000000012EEEEEEEEEEEEEEEEEEEE100001400000005678
# B000000000000000000000000012EEEEEEEEEEEEEEEEEEEE100001400000005678