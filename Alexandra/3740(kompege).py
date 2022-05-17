# a -> камни в 1ой кучи
# с -> номер хода
# m -> номер хода того игрока, который должен победить

def f(a, c, m):
    if a >= 166:
        return c == m
    if c > m:
        return 0
    h = []
    for i in range(1, 166):
        if a * i <= 166:
            h.append(f(a * i, c + 1, m))
        else:
            break
    h.extend([f(a + 10, c + 1, m), f(a + 2, c + 1, m)])
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for i in range(1, 166):
    if f(i, 0, 3):
        print(i)

# 19 -> 4
# 20 -> 7 18
# 21 ->