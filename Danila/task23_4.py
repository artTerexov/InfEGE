# https://inf-ege.sdamgia.ru/problem?id=15932

def calc(n, f):
    if n == 44 and f == 1:
        return 1
    if n > 44:
        return 0
    if n == 29:
        return 0
    if n == 13:
        f += 1
    return calc(n + 1, f) + calc(n * 2, f) + calc(n * 3, f)


print(calc(2, 0))