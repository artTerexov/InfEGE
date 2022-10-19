# Варя составляет пятизначные числа в шестнадцатиричной системе счисления, в
# которых цифры расположены в порядке неубывания. Сколько различных чисел может составить Варя?

import itertools

s = "0123456789ABCDEF"

a = set(itertools.product(s, repeat=5))
count = 0

for el in a:
    minimum = el[0]
    flag = True
    for i in range(1, len(el)):
        if el[i] >= minimum:
            minimum = el[i]
            continue
        else:
            flag = False
            break
    if flag and el[0] != "0":
        print(el)
        count += 1
print(count)
