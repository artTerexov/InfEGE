# Петя составляет семибуквенные слова перестановкой букв слова ТРАТАТА.
# Сколько всего различных слов может составить Петя?

import itertools

a = set(itertools.permutations("ТРАТАТА", r=7))
count = 0

for i in a:
    count += 1
print(count)