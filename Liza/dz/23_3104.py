# 1. прибавь 1
# 2. увеличь каждый разряд числа на 1
# Например, число 23 с помощью команды 2 превратится в 34, а 29 в 39
# (так как младший разряд нельзя увеличить). Если перед выполнением команды 2 какая-либо цифра равна 9,
# она не изменяется. Сколько есть программ, которые число 24 преобразуют в число 46?


def calc(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return calc(start + 1, end) + calc(f(start), end)


def f(c):
    a = str(c)
    b = ''
    for i in range(len(a)):
        if a[i] != '9':
            b += str(int(a[i]) + 1)
        else:
            b += a[i]
    return int(b)


print(calc(24, 46))
