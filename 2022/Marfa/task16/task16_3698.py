def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + f(n/2-3)
    if n > 5 and n % 8 != 0:
        return n + f(n+4)


for i in range(1, 101):
    try:
        f(i)
        print(i)
    except RecursionError:
        continue
