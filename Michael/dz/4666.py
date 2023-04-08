with open("4666") as f:
    a = [int(i) for i in f.readlines()]

middle = sum(a) / len(a)


c = 0
m = 0
for i in range(len(a) - 1):
    if (a[i] < middle or a[i + 1] < middle) and ((a[i] % 3 == 0 and a[i] % 5 != 0 and a[i] % 11 != 0 and a[i] % 19 != 0) or (a[i + 1] % 3 == 0 and a[i + 1] % 5 != 0 and a[i + 1] % 11 != 0 and a[i + 1] % 19 != 0)):
        c += 1
        m = max(m, a[i] + a[i + 1])

print(c, m)