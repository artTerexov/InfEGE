import functools

@functools.lru_cache(maxsize=None)
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return F(n // 2)


count = 0
for i in range(1000000000):
    # c = 0
    if F(i) == 3 or i % 7 == 0 or i % 11 == 0 or i % 13 == 0:
        print(i)
        count += 1
print(count)
