# Аня составляет слова, переставляя буквы в слове ОДЕКОЛОН, избегая слов,
# где соседние буквы — одинаковые. Сколько различных слов, включая исходное,
# может составить Аня?

import itertools

s = "ОДЕКОЛОН"
a = set(itertools.permutations(s, r=8))
counter = 0

for i in a:
    n = "".join(i)
    if "ОО" not in n:
        counter += 1

print(counter)
