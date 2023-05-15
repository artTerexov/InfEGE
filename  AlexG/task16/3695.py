def F(n):
    if n <= 5:
        return n
    if n > 5 and n % 3 == 0:
        return n + F((n/3) + 2)
    if n > 5 and n % 3 != 0:
        return n + F(n + 3)


for i in range(1, 1000):
    try:
        if F(i) > 1000:
            print("Ответ", i)
            break
    except RecursionError:
        print("Ошибка при значении", i)