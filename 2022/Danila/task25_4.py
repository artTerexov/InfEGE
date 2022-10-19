# https://inf-ege.sdamgia.ru/problem?id=29673


for i in range(123456789, 223456790):
    b = []
    if int(i ** 0.5) ** 2 != i:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            b.append(j)
            if not((i // j) in b):
                b.append(i // j)
        if len(b) > 3:
            break
    if len(b) == 3:
        print(i, max(b))

# 1
# 2
# 4
# 3089
# 6178
# 12356