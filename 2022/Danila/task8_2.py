# Петя составляет шестибуквенные слова перестановкой букв слова ЧИУАУА.
# Сколько всего различных слов может составить Петя?

import itertools

a = set(itertools.permutations("ЧИУАУА", r=6))
count = 0
for i in a:
    count += 1
print(count)