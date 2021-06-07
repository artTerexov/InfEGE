n = int(input())
f = n
m = 1
while f > 0:
    for i in range(m):
        if f > 0:
            print(m, end=" ")
        f = f - 1
    m = m + 1