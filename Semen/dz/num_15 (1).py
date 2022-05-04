def dell(x, a):
    return ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 70)


for A in range(1, 1000):
    if all([dell(x, A) for x in range(1, 1000)]):
        print(A)
        break
