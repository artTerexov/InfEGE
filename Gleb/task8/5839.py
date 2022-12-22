# Дмитрий составляет слова, переставляя буквы в слове АМФИБРАХИЙ. Сколько слов,
# в которых есть, хотя бы, 2 подряд идущие гласные может составить Дмитрий?

from itertools import permutations


a = set(permutations('АМФИБРАХИЙ', r=10))
count = 0
for i in a:
    el = ''.join(i)
    if 'АИ' in el or 'ИА' in el or 'АА' in el or 'ИИ' in el:
        count += 1
print(count)