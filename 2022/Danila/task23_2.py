# https://inf-ege.sdamgia.ru/problem?id=13418

def calc(n):
    if n == 27:
        return 1
    if n > 27:
        return 0
    if n == 26:
        return 0
    return calc(n + 1) + calc(2*n + 1)


print(calc(1))