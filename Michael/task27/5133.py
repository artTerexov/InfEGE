def F(n, M):
    c = 0
    multiplier = 1
    for i in range(len(n)):
        if (multiplier * n[i]) % M != 0:
            c += 1
            multiplier *= n[i]
            for j in range(i + 1, len(n)):
                if (multiplier * n[j]) % M != 0:
                    c += 1
                    multiplier *= n[j]
                else:
                    multiplier = 1
                    break
    return c


# with open("files/5133_A") as f:
#     a = [int(i) for i in f.readlines()]
#
# print(F([3, 17, 20, 1], 20))
# print(F(a, 858967))

with open("files/5133_B.txt") as f:
    a = [int(i) for i in f.readlines()]

print(F(a, 858967))
