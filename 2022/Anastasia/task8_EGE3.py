# (№ 4238) (А. Куканова) Ася составляет 7-буквенные слова из букв А, П, Е, Л, Ь, С, И, Н. Все буквы
# слова различны.
# Буква Ь, если встречается, стоит между двумя согласными. Сколько таких слов может составить Ася?

import itertools

a = set(itertools.permutations('АПЕЛЬСИН', r=7))
count = 0

for i in a:
    b = ''.join(i)
    if 'Ь' in b:
        index = b.find('Ь')
        if index != 0 and index != len(b) - 1:
            if b[index - 1] in 'ПЛСН' and b[index + 1] in 'ПЛСН':
                count += 1
    else:
        count += 1
print(count)


# ПАНАНАНЬЛ
