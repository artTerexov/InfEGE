# Миша составляет 5-буквенные коды из букв К, О, Р, Н, Е, Т. Каждая допустимая
# гласная буква может входить в
# код не более одного раза. Сколько кодов может составить Миша?

import itertools

a = set(itertools.product("КОРНЕТ", repeat=5))
count = 0
for i in a:
    if i.count("О") <= 1 and i.count("Е") <= 1:
        count += 1
print(count)