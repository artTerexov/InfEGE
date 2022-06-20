# Определите количество пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых ровно одна цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.


import itertools

a = set(itertools.product('01234567', repeat=5))
count = 0

for i in a:
    b = ''.join(i)
    if b[0] != '0' and b.count('6') == 1 and '61' not in b and '16' not in b and '36' not in b and '63' not in b and '56' not in b and '65' not in b and '76' not in b and '67' not in b:
        count += 1
print(count)