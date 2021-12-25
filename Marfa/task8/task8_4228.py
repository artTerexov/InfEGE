# Маша составляет четырёхбуквенные слова из букв A, B, C, D, E, причём сначала в слове
# должны быть расположены гласные в алфавитном порядке, затем согласные в обратном алфавитном
# порядке. Буквы могут повторяться. Слово может состоять только из гласных или только из
# согласных. Пример подходящего слова: AAEDC. Сколько различных слов может составить Маша?

import itertools
co = 0
a = "ABCDE"
b = set(itertools.product(a, repeat=4))
for i in b:
    c = ''.join(i)
    flag = True
    for j in range(len(c) - 1):
        if c[j] == 'E' and 'A' in c[j + 1:]:
            flag = False
            break
        if c[j] == 'B' and ('D' in c[j + 1:] or 'C' in c[j + 1:] or 'A' in c[j + 1:] or 'E' in c[j + 1:]):
            flag = False
            break
        if c[j] == 'C' and ('D' in c[j + 1:] or 'A' in c[j + 1:] or 'E' in c[j + 1:]):
            flag = False
            break
        if c[j] == 'D' and ('A' in c[j + 1:] or 'E' in c[j + 1:]):
            flag = False
            break
    if flag:
        co += 1
print(co)
