# Миша составляет 5-буквенные коды из букв К, А, Л, Ь, К, А.
# Каждая допустимая гласная буква может входить в код не более одного раза.
# Сколько кодов может составить Миша?
import itertools
# from itertools import *

s = "КАЛЬ"

a = itertools.product(s, repeat=5)
count = 0

for i in a:
    if i.count("А") <= 1:
        count += 1

print(count)