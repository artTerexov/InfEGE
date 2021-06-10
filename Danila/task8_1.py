# Петя составляет 6-буквенные слова из букв К, О, М, Е, Т, А.
# Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд
# две гласные или две согласные. Сколько различных кодов может составить Петя?

import itertools

a = set(itertools.permutations("КОМЕТА", r=6))
count = 0

for i in a:
    b = "".join(i)
    if not("ОЕ" in b or "ЕО" in b or "ЕА" in b or "АЕ" in b or "АО" in b or "ОА" in b):
        if not ("КМ" in b or "МК" in b or "МТ" in b or "ТМ" in b or "КТ" in b or "ТК" in b):
            count += 1

print(count)