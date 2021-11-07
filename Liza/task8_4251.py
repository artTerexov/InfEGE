# Маша составляет 6-буквенные слова из букв З, Е, Р, К, А, Л, О, содержащие букву К, но не более 4 раз.
# Остальные буквы не могут повторяться. Сколько различных слов может составить Маша?

import itertools

s = "ЗЕРКАЛО"
a = set(itertools.product(s, repeat=6))
count = 0

for i in a:
    b = "".join(i)
    if b.count("К") < 5 and b.count("Е") < 2 and b.count("З") < 2 and b.count("Р") < 2 and b.count("А") < 2 and b.count("Л") < 2 and b.count("О") < 2:
        count += 1
print(count)
