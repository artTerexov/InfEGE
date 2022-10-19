# Текстовый файл 24-s1.txt состоит не более чем из 106 заглавных латинских букв (A..Z).
# Текст разбит на строки различной длины. Определите количество строк, в которых буква J
# встречается чаще, чем буква E.

s = open("24-s1.txt").read()

countJ = 0
countE = 0
count = 0

for i in s:
    if i == "E":
        countE += 1
    if i == "J":
        countJ += 1
    if i == "\n":
        if countJ > countE:
            count += 1
        countJ = 0
        countE = 0
print(count)