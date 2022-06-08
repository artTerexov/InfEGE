a = 18 ** 105 + 25 * 16 ** 100 - 3 ** 51
base = 16
s = ''
n = '0123456789abcdef'
while a > 0:
    s = n[a % base] + s
    a //= base

print(s)

