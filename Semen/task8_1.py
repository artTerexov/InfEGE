# Миша составляет 5-буквенные коды из букв К, А, Л, Ь, К, А. Каждая допустимая
# гласная буква может входить в код не более одного раза. Сколько кодов может составить Миша?

import itertools

s = "КАЛЬКА"

a = set(itertools.product(s, repeat=5))

count = 0

for i in a:
    print(i)
    if i.count("А") <= 1:
        count += 1

print(count)

