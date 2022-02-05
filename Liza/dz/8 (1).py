# Лида составляет слова из букв С, Е, П, И, Я. Каждая гласная буква встречается в слове не более двух раз.
# Каждая согласная может стоять в слове на первой позиции, либо не встречаться вовсе.
# Сколько слов длиною более двух символов может составить Лида?

import itertools


a = 'СЕПИЯ'
buff = []
cons = 'СП'

for k in range(3, 8):
    words = set(itertools.product(a, repeat=k))
    for i in words:
        if i.count('Е') > 2 or i.count('И') > 2 or i.count('Я') > 2:
            continue
        else:
            flag = 1
            for l in range(1, len(i)):
                if i[l] in cons:
                    flag = 0
                    break
            if flag:
                buff.append(i)

print(len(buff))