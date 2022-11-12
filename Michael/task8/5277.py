from itertools import product

a = list(product('АИКЛМЬ', repeat=6))
a.sort()

for i in a:
    el = ''.join(i)


print('AFC' > 'ACDBDH')