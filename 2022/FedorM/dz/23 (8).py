def func(x):
    return 2 ** (len(bin(x)[2:]) - 1) if bin(x)[2:].count('1') > 1 else 0


def f(x):
    if x == int('100', 2):
        return 1
    if x < int('100', 2):
        return 0
    return f(x - 1) + f(func(x))

# 1011 -> 1000


# print(bin(2 ** (len("11100") - 1))[2:])

print(f(int('1100', 2)))


