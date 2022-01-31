# Текстовый файл 24-j2.txt состоит не более чем из 106 символов F, A, I, L.
# Определите максимальное количество подряд идущих одинаковых букв.

with open('24-j2.txt') as f:
    s = f.read()

count = 1
maxcount = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 1

print(maxcount)