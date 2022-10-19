# Текстовый файл 24-s1.txt состоит не более чем из 106
# заглавных латинских букв (A..Z). Текст разбит на строки различной длины.
# Определите количество строк, в которых встречается комбинация A*R,
# где звёздочка обозначает любой символ.

f = open("24-s1.txt")
s = f.read()
f.close()

count = 0
stringCount = 0

for i in range(0, len(s)):
    if s[i] == "A" and s[i + 2] == "R" and s[i + 1] != "\n":
        count += 1
    if s[i] == "\n":
        if count != 0:
            stringCount += 1
        count = 0

print(stringCount)
