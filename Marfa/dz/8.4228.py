# Маша составляет четырёхбуквенные слова из букв A, B, C, D, E,
# причём сначала в слове должны быть расположены гласные в алфавитном порядке,
# затем согласные в обратном алфавитном порядке. Буквы могут повторяться.
# Слово может состоять только из гласных или только из согласных.
# Сколько различных слов может составить Маша?

import itertools
co = 0
a = "ABCDE"
b = set(itertools.product(a, repeat=4))
for i in b:
    c = ''.join(i)
    n = 1
    for j in range(len(c) - 1):
        if c[j] == "A" and (c[j + 1] == "A" or c[j + 1] == "E" or c[j + 1] in "BCD"):
            n += 1
        elif c[j] == "E" and (c[j + 1] == "E" or c[j + 1] in "BCD"):
            n += 1
        elif c[j] == "B" and c[j + 1] == "B":
            n += 1
        elif c[j] == "C" and (c[j + 1] == "B" or c[j + 1] == "C"):
            n += 1
        elif c[j] == "D" and (c[j + 1] == "B" or c[j + 1] == "C" or c[j + 1] == "D"):
            n += 1
        else:
            break
    if n == 4:
        co += 1
    # if c.count('A') == 0 and c.count('E') == 0 and c.count('DB') == 0 and c.count('DC') == 0 and c.count('CB') == 0:
    #     print(c)
    #     co += 1
    # if c.count('EA') == 0 and c.count('B') == 0 and c.count('C') == 0 and c.count('D') == 0:
    #     print(c)
    #     co += 1
print(co)

# 20
