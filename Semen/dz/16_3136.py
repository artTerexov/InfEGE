def F(n):
    global b
    b = b + (n - 5)
    if n > 1:
        b = b + (n + 8)
        F(n - 2)
        F(n - 3)


for i in range(1, 10000):
    b = 0
    F(i)
    if b > 3200000:
        print(i)
        break
