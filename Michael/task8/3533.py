# Вася составляет 4-буквенные слова из букв И, Н, С, Т, А, В, К и упорядочивает их по алфавиту.
# При этом на первом месте может быть только согласная, на последнем - гласная. Вот начало списка:
# 1. ВААА
# 2. ВААИ
# 3. ВАВА
# ...
# Укажите номер слова НИКА в этом списке.


import itertools

glas = 'ИА'
sogl = 'НСТВК'

a = set(itertools.product('ИНСТАВК', repeat=4))
buff = []

for i in a:
    b = ''.join(i)
    if b[0] in sogl and b[-1] in glas:
        buff.append(b)

buff.sort()
print(buff)
print(buff.index('НИКА'))

