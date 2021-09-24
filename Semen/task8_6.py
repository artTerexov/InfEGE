# Мила составляет 4-значные числа в 8-ичной системе. Сколько различных чисел, делящихся на 4
# без остатка, может составить Мила?

import itertools

s = "01234567"
a = set(itertools.permutations(s, r=4))
count = 0

for i in a:
    b = "".join(i)

print(count)