def convert(x, n):
    digits = ""
    while x:
        digits += str(x % n)
        x //= n
    return digits[:: -1]


a = (64 ** 25 + 4 ** 10) - (16 ** 20 + 32 ** 3)
print(convert(a, 4))
