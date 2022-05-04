# Текстовый файл 24-197.txt содержит строку из заглавных латинских букв X, Y и Z,
# всего не более чем из 106 символов. Определите максимальное количество идущих подряд троек
# символов X*Y или Z*Y, где * обозначает один любой символ.

with open ('files/5041.txt') as f:
    s = f.read()
big = [0, 0, 0]
count = [0, 0, 0]
# s = s.replace('XZY', 't')
# s = s.replace('XXY', 't')
# s = s.replace('XYY', 't')
# s = s.replace('ZZY', 't')
# s = s.replace('ZXY', 't')
# s = s.replace('ZYY', 't')
for i in range(0, len(s) - 4, 3):
    if (s[i] == 'X' or s[i] == 'Z') and s[i + 2] == 'Y':
        count[0] += 1
    else:
        big[0] = max(big[0], count[0])
        count[0] = 0
    if (s[i + 1] == 'X' or s[i + 1] == 'Z') and s[i + 3] == 'Y':
        count[1] += 1
    else:
        big[1] = max(big[1], count[1])
        count[1] = 0
    if (s[i + 2] == 'X' or s[i + 2] == 'Z') and s[i + 4] == 'Y':
        count[2] += 1
    else:
        big[2] = max(big[2], count[2])
        count[2] = 0

print(big)

# XZYYZXYZXYZXYZYYZXYZXYZYYZYYZXYZYYZYYZXYZXYZYYZXYZXYZYYZXYZXY