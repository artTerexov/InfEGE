# Петя составляет шестибуквенные слова перестановкой букв слова КАБАЛА. При этом
# он избегает слов с двумя подряд одинаковыми
# буквами. Сколько всего различных слов может составить Петя?

import itertools

a = set(itertools.permutations("КАБАЛА", r=6))
count = 0
for i in a:
    b = "".join(i)
    if not("АА" in b):
        count += 1
print(count)