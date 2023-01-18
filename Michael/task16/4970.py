import functools
import time

start_time = time.time()


@functools.cache
def F(n):
    if n == 0:
        return 8
    if n > 0 and n % 3 == 0:
        return 5 + F(n // 3)
    else:
        return F(n // 3)


c = 0

for i in range(1, 100000000):
    if F(i) == 18:
        c += 1
print(c)

print("--- %s seconds ---" % (time.time() - start_time))
