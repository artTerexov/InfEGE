# Петя составляет шестибуквенные слова перестановкой букв слова АВРОРА. При
# этом он избегает слов с двумя подряд одинаковыми буквами. Сколько
# всего различных слов может составить Петя?

import itertools

s = "АВРОРА"

a = set(itertools.permutations(s, r=6))
count = 0
for i in a:
    b = "".join(i)
    if not("АА" in b or "РР" in b):
        count += 1

print(count)