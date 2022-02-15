b = []
s = 0
for a in range(586132, 586430 + 1):
    d = set()
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            d.add(i)
            d.add(a//i)
    if len(d) == 80:
        print(d)
    # if len(d) > s:
    #     b.clear()
    #     s = len(d)
    #     b.append(list(d))
    # elif len(d) == s:
    #     b.append(list(d))
# b[0].sort()
# b[-1].sort()
# print(s, b[0][-2])
# print(s, b[-1][-2])

# 80 293112
# 80 293160