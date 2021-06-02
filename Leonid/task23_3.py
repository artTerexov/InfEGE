# 2->15  содержит 7 и не содержит 10
# +1 +3 *2

def calc(n, f):
    if n > 15:
        return 0
    if n == 15 and f == 1:
        return 1
    if n == 10:
        return 0
    if n == 7:
        f += 1
    return calc(n + 1, f) + calc(n + 3, f) + calc(n * 2, f)


print(calc(2, 0))