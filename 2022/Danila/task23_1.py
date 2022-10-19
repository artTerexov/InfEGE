# https://inf-ege.sdamgia.ru/problem?id=3607

def calc(n):
    if n == 50:
        return 1
    if n > 50:
        return 0
    return calc(n + 2) + calc(n * 5)


print(calc(2))