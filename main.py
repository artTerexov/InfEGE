a = 17445800000
d = set()
for n in range(2, int(a ** 0.5) + 1):
    if a % n == 0:
        d.add(n)
        d.add(a // n)

print(len(d))

