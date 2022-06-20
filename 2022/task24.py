a = open('24.txt').read()

l1 = 'BCD'
l2 = 'AO'
count = 0
maxC = 0

for i in range(0, len(a) - 1, 2):
    if a[i] in l1 and a[i + 1] in l2:
        count += 1
        maxC = max(count, maxC)
    else:
        count = 0
print(maxC)
