with open('files/27-B_1396.txt') as f:
    N = int(f.readline())
    a = [[int(j) for j in i.split()] for i in f.readlines()]
k = [0]
l = 123
for i in range(len(a)):
    comb = {x + y for x in a[i] for y in k}
    if 2553076396 in comb:
        print('OOO')
    if i == (len(a) - 1):
        k = {x % l: x for x in sorted(comb, reverse=True)}
    else:
        k = {x % l: x for x in sorted(comb, reverse=True)}.values()
print(k)
