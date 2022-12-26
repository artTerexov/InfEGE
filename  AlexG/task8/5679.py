# Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только
# слова с различными буквами в начале и в конце. Сколько различных слов может составить Оля?

from itertools import permutations

a = set(permutations('СПОРТЛОТО', r=9))
count = 0
for i in a:
    b = ''.join(i)
    if b[0] != b[-1]:
        count += 1

print(count)

