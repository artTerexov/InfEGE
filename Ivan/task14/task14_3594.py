# Сколько единиц в двоичной записи числа 2^2014 – 4^650 – 38?

num = 2 ** 2014 - 4 ** 650 - 38
base = 2

result = ""

while num != 0:
    result += str(num % base)
    num = num // base

print(result.count("1"))

# 1313123132000000000