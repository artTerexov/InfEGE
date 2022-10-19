# Сколько существует различных символьных последовательностей длины 3 в четырёхбуквенном алфавите
# {A,B,C,D}, если известно, что одним из соседей A обязательно является D,
# а буквы B и C никогда не соседствуют друг с другом?

import itertools

a = 'ABCD'
b = set(itertools.product(a, repeat=3))
buff = []

for i in b:
    d = ''.join(i)
    if 'A' in d:
        if ('AD' in d or 'DA' in d) and not ('BC' in d or 'CB' in d):
            buff.append(i)
    else:
        if not('BC' in d or 'CB' in d):
            buff.append(i)
print(buff)
print(len(buff))
