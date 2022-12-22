# Определите количество чисел, девятеричная запись которых содержит ровно 6 цифр, из которых не более двух нечётных,
# а сумма всех цифр этой записи кратна 6, но не кратна 4
import itertools


def perevod(num: int, base: int) -> str:
    N = ""
    while num > 0:
        N = N + str(num % base)
        num = num // base
    return N[::-1]


def count_n(a) -> bool:
    z = 0
    for i in a:
        if i in "1357":
            z += 1
    return z < 3


c = 0
for x in range(59049, 531440 + 1):
    n = perevod(x, 9)
    v = count_n(n)
    if len(n) == 6 and v:
        s = 0
        for j in n:
            s += int(j)
        if s % 6 == 0 and s % 4 != 0:
            c += 1
print(c)

