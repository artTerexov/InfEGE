def calc(n, f):
    # блогоприятное условие (return 1)
    if n == 29 and f == 1:
        return 1
    # неблогоприятное условие (return 0)
    if n > 29 or n == 25:
        return 0
    if n == 14:
        f += 1
    # основная часть
    return calc(n + 1, f) + calc(n * 2, f)


print(calc(2, 0))