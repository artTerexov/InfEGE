# a -> камни в 1ой кучи
# с -> номер хода
# m -> номер хода того игрока, который должен победить

def f(a, c, m):
    if a == 1 and c != 0:
        return c % 2 == m % 2
    if c == m or a < 1:
        return 0
    h = [f(a // 2 if a % 2 == 0 else a - 2, c + 1, m), f(a // 3 if a % 3 == 0 else a - 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for i in range(1, 38):
    if f(i, 0, 4):
        print(i)

# 19 -> 4
# 20 -> 7 18
# 21 ->