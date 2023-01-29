from itertools import product


a = set(product('ДКМО', repeat=5))

a = sorted(a)

a = [''.join(i) for i in a]

print(a.index('КОМОД') - a.index('ДОМОК') + 1)


