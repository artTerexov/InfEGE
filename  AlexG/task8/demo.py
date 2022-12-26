from itertools import product


a = set(product('01234567', repeat=5))
count = 0
for i in a:
    b = ''.join(i)
    # 61 63 65 67 16 36 56 76
    if b.count('6') == 1 and not('61' in b or '63' in b or '65' in b or '67' in b or '16' in b or '36' in b or '56' in b or '76' in b) and b[0] != '0':
        count += 1

print(count)
