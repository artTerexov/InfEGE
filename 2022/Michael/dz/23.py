def first_command(n):
    n = str(n)
    s = 0
    for i in n:
        s += int(i)
    return s


def second_command(n):
    n = str(n)
    p = 1
    for i in n:
        p *= int(i)
    return p


def F(n):
    if n == 8:
        return True
    if n < 10:
        return False
    return F(first_command(n)) + F(second_command(n))


k = 0
for i in range(1, 100):
    if F(i):
        k += 1
print(k)