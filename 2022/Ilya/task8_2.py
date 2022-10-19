# Петя составляет семибуквенные слова перестановкой букв слова АССАСИН.
# Сколько всего различных слов может составить Петя?

import itertools

s = "АССАСИН"

a = set(itertools.permutations(s, r=7))

count = 0
for i in a:
    b = "".join(i)
    if not("ИА" in b or "АА" in b or "АИ" in b):
        count += 1
print(count)
