# Миша составляет 6-буквенные коды из букв С, А, Л, Ь, С, А. Каждая допустимая гласная
# буква может входить в код не более одного раза. Сколько кодов может составить Миша?

import itertools

s = "САЛЬСА"

a = set(itertools.product(s, repeat=6))
count = 0

for i in a:
    if i.count("А") <= 1:
        count += 1
print(6 * 3 ** 5 + 3 ** 6)
print(count)

