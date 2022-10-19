import itertools

a = set(itertools.product('0123456', repeat=7))
count = 0

for i in a:
    b = ''.join(i)
    print(b)
    if b[0] != '0' and b[0] != '3' and b[0] != '5' and not('22' in b and '44' in b):
        count += 1

print(count)
