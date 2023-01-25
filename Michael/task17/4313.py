def perevod(num: int, base: int) -> str:
    N = ""
    while num > 0:
        N = N + str(num % base)
        num = num // base

    return N[::-1]


def two(n):
    x = bin(n)[2:]
    if x[-4::] == "1001":
        return True
    else:
        return False


def fifth(m):
    z = perevod(m, 5)
    if z[-2::] == "11":
        return True
    else:
        return False


with open("files/4313") as f:
    a = [int(i) for i in f.readlines()]

c = 0
maxx = 0
for j in a:
    if two(j) and fifth(j):
        maxx = max(j, maxx)
        c += j
print(maxx, c)
