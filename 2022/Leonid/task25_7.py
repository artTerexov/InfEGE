# https://inf-ege.sdamgia.ru/problem?id=29673

for i in range(123456789, 223456789):
    buff = []
    if int(i ** 0.5) ** 2 != i:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            buff.append(j)
            if j != i // j:
                buff.append(i // j)
        if len(buff) > 3:
            break
    if len(buff) == 3:
        print(i, max(buff))
