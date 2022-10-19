import itertools

a = "МИМИКРИЯ"
b = set(itertools.permutations(a, r=8))
count = 0

for i in b:
    c = "".join(i)
    count += 1
print(count)

