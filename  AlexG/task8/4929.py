from itertools import product

a = set(product('012345678', repeat=7))
count = 0
for i in a:
    b = ''.join(i)
    if b[0] != '0' and b[0] != '2' and b[0] != '4' and b[0] != '6' and (b[-1] != b[-2] or b[-3] != b[-2] or b[-1] != b[-3]):
        count += 1
print(count)


