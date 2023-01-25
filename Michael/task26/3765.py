def double(x):
    middle = x[len(x) // 2]
    # 1 2 3 4 5 6
    c = 0
    maxx = 0
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if ((x[i] + x[j]) % 2 == 0) and (middle > ((x[i] + x[j]) // 2)):
                c += 1
                # print(n1, n2)
                maxx = max((x[i] + x[j]) // 2, maxx)

    return c, maxx


with open("files/3765") as s:
    a = [int(i) for i in s.readlines()]
    a.sort()

# print(double(sorted([3, 8, 14, 11, 2])))
print(double(a))

# 3183529, 56263918

# 3183530, 56263940
