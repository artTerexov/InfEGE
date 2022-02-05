# (№ 3538) (Е. Джобс) Все 4-буквенные слова, составленные из букв П, Р, В, Д, А, записаны в алфавитном порядке и пронумерованы. Вот начало списка:
# 1. АААА
# 2. АААВ
# 3. АААД
# 4. АААП
# 5. АААР
# 6. ААВА
# ...
# Найдите номер первого слова в этом списке, которое не содержит гласных и одинаковых букв.

import itertools

a = set(itertools.product('ПРАВДА', repeat=4))
buff = []

for i in a:
    buff.append(''.join(i))

buff.sort()

print(buff.index('ВДПР') + 1)