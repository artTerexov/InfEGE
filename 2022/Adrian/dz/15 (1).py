def F(x, a):
    return ((x % 15 != 0) or (x % 28 != 0) or (x % a == 0)) and (a > 70)
for a in range(1, 1000):
    if all(F(x, a) == 1 for x in range(1, 1000)):
        print(a)
        break
    
