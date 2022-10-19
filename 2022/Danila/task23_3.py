# https://inf-ege.sdamgia.ru/problem?id=11358

def calc(n, f):
    if n == 12 and f == 1:
        return 1
    if n > 12:
        return 0
    if n == 10:
        f += 1
    return calc(n + 1, f) + calc(n + 2, f) + calc(n * 2, f)


print(calc(3, 0))