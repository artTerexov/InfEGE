import itertools

s = 'ЧИУАУА'
a = set(itertools.permutations(s, r=6))
count = 0
for i in a:
    count += 1

print(count)