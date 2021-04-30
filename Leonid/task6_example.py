
for i in range(0, 100000):
    s = i
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(i)



