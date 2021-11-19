# МАРИНА из букв своего имени составляет слова перестановкой исходных букв.
# Сколько различных слов может составить МАРИНА, если первая буква не может быть гласной?

import itertools

a = set(itertools.permutations("МАРИНА", r=6))
count = 0

for i in a:
    b = "".join(i)
    if b[0] not in "АИ":
        count += 1

print(count)