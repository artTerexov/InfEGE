def is_simple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


b = []
for i in range(278932, 325397):
    buff = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if is_simple(j):
                buff.add(j)
            if is_simple(i // j):
                buff.add(i // j)
    buff = list(buff)
    if len(buff) == 3 and buff[0] * buff[1] * buff[2] == i and buff[0] % 10 == buff[1] % 10 == buff[2] % 10:
        b.append(i)

print(len(b), max(b))