from string import hexdigits

b = "Hello semen"

# Функция перевода из 10 в любую сс
def calc(x, y):
    s = ""
    while x > 0:
        s += hexdigits[x % y]
        x = x // y
    return s[::-1]


