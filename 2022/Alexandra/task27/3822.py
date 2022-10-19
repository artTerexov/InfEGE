with open('files/3822_B.txt') as f:
    s = [int(i) for i in f.read().split()][1:]

k = [0, 0, 0]

for i in s:
    k1 = k.copy()
    ostat = i % 3
    for j in range(3):
        if k[j] != 0:
            k[(j + ostat) % 3] += k1[j]
    k[ostat] += 1

print(k[0])

# 5 [5, 4, 6]

# [5, 7, 6]

a = [1, 2, 3]
a[0] = 4
print(a)