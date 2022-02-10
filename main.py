count = 0
for a in range(3532000, 3532160 + 1):
    d = set()
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            d.add(i)
            d.add(a // i)
    if len(d) == 2:
        count += 1
        print(count, a)

# 1 3532007
# 2 3532019
# 3 3532021
# 4 3532033
# 5 3532049
# 6 3532091
# 7 3532103
# 8 3532121
# 9 3532147
