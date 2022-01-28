def F(n):
    k = 0
    k += n - 5
    if n > 1:
        k += n + 8
        F(n - 2)
        F(n - 3)


for i in range(1, 2):
    print(F(i))
