import itertools

a = set(itertools.permutations('ПАРАБОЛА', r=8))
glas = 'АО'
soglas = 'ПРБЛ'
b = set(itertools.permutations(soglas, r=2))
print(len(b))
count = 0

for i in a:
    b = ''.join(i)
    flag = True
    for j in range(len(b) - 1):
        if (b[j] in soglas and b[j + 1] in soglas) or (b[j] in glas and b[j + 1] in glas):
            flag = False
            break
    if flag:
        count += 1

print(count)

