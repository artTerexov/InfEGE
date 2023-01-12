from itertools import permutations

a = set(permutations('АКАРИДА', r=7))
count = 0
for i in a:
    b = ''.join(i)
    # if b.count('АИ') == 0 and b.count('АА') == 0 and b.count('ИА') == 0 and b.count('РК') == 0 and b.count('КР') == 0 and b.count('ДК') == 0 and b.count('КД') == 0 and b.count('ДР') == 0 and b.count('РД') == 0:
    #     count += 1
    flag = True
    for j in range(len(b) - 1):
        if (b[j] in 'АИ' and b[j + 1] in 'АИ') or (b[j] in 'КРД' and b[j + 1] in 'КРД'):
            flag = False
            break
    if flag:
        count += 1
print(count)

# AA АИ ИА
# КР РК РД ДР
