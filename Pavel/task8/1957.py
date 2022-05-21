# (А.Н. Носкин) Петя составляет шестибуквенные слова перестановкой букв
# слова ТАРТАР. Сколько всего различных слов может составить Петя?

from itertools import permutations

a = set(permutations('ТАРТАР', r=6))
count = 0

for i in a:
    count += 1

print(count)