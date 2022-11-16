# Вася составляет 6-буквенные коды из букв П, А, Н, Е, Л, Ь.
# Каждую букву нужно использовать ровно 1 раз, при этом код не может начинаться с буквы Ь и
# не может содержать сочетания ЕАП. Сколько различных кодов может составить Вася?

import itertools

a = set(itertools.permutations("ПАНЕЛЬ", r=6))
count = 0

for i in a:
    b = ''.join(i)
    if b[0] != "Ь" and "ЕАП" not in b:
        count += 1
print(count)