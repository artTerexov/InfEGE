# Миша составляет 6-буквенные коды из букв С, А, Л, Ь, С, А.
# Каждая допустимая гласная буква может входить в код не более одного раза.
# Сколько кодов может составить Миша?

import itertools

a = set(itertools.product("САЛЬСА", repeat=6))
count = 0

for i in a:
    b = "".join(i)
    if b.count("А") <= 1:
        count += 1

print(count)