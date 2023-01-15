from itertools import product

a = product('012345678', repeat=5)
count = 0

for i in a:
    b = ''.join(i)
    if b[0] not in '01357' and b[4] not in '18' and b.count('3') < 2:
        count += 1
print(count)

# ('2', '3', '2', '3', '2') -> '23232'