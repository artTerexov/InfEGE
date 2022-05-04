def f(x):
    return ((x % a != 0) and (x % 6 == 0)) <= (x % 3 != 0)


for a in range(1, 500):
    if all(f(x) == 1 for x in range(1, 500)):
        print(a)