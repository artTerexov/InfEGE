# (А. Куканова) Маша составляет четырёхбуквенные слова из букв A, B, C, D, E,
# причём сначала в слове должны быть расположены гласные в алфавитном порядке,
# затем согласные в обратном алфавитном порядке. Буквы могут повторяться.
# Слово может состоять только из гласных или только из согласных.
# Пример подходящего слова: AAEDC. Сколько различных слов может составить Маша?

import itertools

a = set(itertools.product("ABCDE", repeat=4))
count = 0
cons = "BCD"

for i in a:
    b = "".join(i)
    flag = True
    for j in range(len(b)):
        if b[j] == "E" and "A" in b[j + 1:]:
            flag = False
            break
        if b[j] == "C" and "D" in b[j + 1:]:
            flag = False
            break
        if b[j] == "B" and ("D" in b[j + 1:] or "C" in b[j + 1:]):
            flag = False
            break
        if (b[j] in cons) and ("A" in b[j + 1:] or "E" in b[j + 1:]):
            flag = False
            break
    if flag:
        count += 1
print(count)

# ADEC