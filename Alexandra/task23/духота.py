import functools


@functools.lru_cache()
def calc(num):
    if num == 42:
        return 1
    if num > 42:
        return 0
    b = []
    for i in num + 1, num + 2, num * 2, num * 3:
        if i not in b:
            b.append(i)
        else:
            b.append(43)
    return calc(b[0]) + calc(b[1]) + calc(b[2]) + calc(b[3])


# 2 -> [3, 4, 4, 6]
print(calc(2))

# 362798265
# 277594601