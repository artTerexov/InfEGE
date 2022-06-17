from itertools import product
count = 0

for i in range(999999959999, 1000000000000, 10):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        d = x % 10
        if d % 3 == 0:
            b += d
        x //= 10
    if a == 12 and b == 99:
        print(i)
        count += 1
print(count)

# 199999999999 -> 12
# 299999999999 -> 12
# 499999999999 -> 12
# 599999999999 -> 12
# 699999999993 -> 132
# 799999999999 -> 12
# 899999999999 -> 12
# 999999999990 -> 11
# 999999999666 -> 220
# Итог 435
print(6 * 12 + 132 + 11 + 220)

c = 0
a = set(product('69', repeat=12))
for i in a:
    b = ''.join(i)
    if b.count('9') == 9 and b.count('6') == 3 and b[0] != '0':
        c += 1

print(c)