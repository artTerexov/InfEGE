x = 64**30 + 2**300 - 4
d = ''
c = 0
while x > 0:
    d = str(x % 8) + d
    x = x // 8
    if d.count('7'):
        c += 1
print(c)