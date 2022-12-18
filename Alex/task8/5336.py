# Определите количество пятизначных чисел, записанных в девятеричной системе счисления,
# которые не начинаются с нечётных цифр, не оканчиваются цифрами 1 или 8, а также содержат
# в своей записи не более одной цифры 3.

from itertools import product


a = set(product('012345678', repeat=5))
count = 0
for i in a:
    b = ''.join(i)
    if int(b[0]) % 2 == 0 and int(b[-1]) != 1 and int(b[-1]) != 8 and b.count('3') <= 1 and b[0] != '0':
        count = count + 1
        # print(b)
print(count)