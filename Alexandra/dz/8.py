import itertools
s = '0123456'
a = sorted(set(itertools.product(s, repeat=4)))
count = 0
count1 = 0
b = []
for i in a:
    n = ''.join(i)
    b.append(n)
b = b[1000:]
for n in b:
    if n.count('00') == 0 and n.count('11') == 0 and n.count('22') == 0 and n.count('33') == 0 and n.count('44') == 0\
            and n.count('55') == 0 and n.count('66') == 0:
        count1 += 1
print(count1)
