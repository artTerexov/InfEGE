def calc(n, f):
    if f == 7:
        b.append(n)
        return 1
    f += 1
    return calc(n + 4, f) + calc(n - 3, f)


b = []
calc(1, 0)
print(set(b))
