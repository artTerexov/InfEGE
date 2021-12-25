def F(n):
    global summa
    summa += 2 * n + 1
    if n > 1:
        summa += 3 * n - 8
        F(n - 1)
        F(n - 4)


for i in range(2, 1000):
    summa = 0
    F(i)
    if summa > 5000000:
        print(i, summa)
        break