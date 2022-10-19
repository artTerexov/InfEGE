# Ася составляет 7-буквенные слова из букв А, П, Е, Л, Ь, С, И, Н. Все буквы слова различны. Буква Ь, если
# встречается, стоит между двумя согласными. Сколько таких слов может составить Ася?

import itertools

a = "АПЕЛЬСИН"
b = set(itertools.permutations(a, r=7))
count = 0

for i in b:
    c = "".join(i)
    index = c.find("Ь")
    if index == -1:
        count += 1
        continue
    if index == len(c) - 1 or index == 0:
        continue
    if c[index - 1] in "ПЛСН" and c[index + 1] in "ПЛСН":
        count += 1
print(count)

# ПЬ
# 12240
