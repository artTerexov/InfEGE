from functools import*


# @lru_cache(maxsize=None)
def f(x, y, z):
    if x == 93 and y == 1 and '11' not in z:
        return 1
    if x > 93 or x == 28:
        return 0
    if x == 10:
        y += 1
    return f(x + 1, y, z + '1') + f(x + 3, y, z + '2') + f(x * 2, y, z + '3')


print(f(4, 0, ''))
