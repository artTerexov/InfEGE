# Текстовый файл 24-5.txt содержит последовательность из символов «(»и «)», всего не более 106 символов.
# Определите максимальное количество подряд идущих пар скобок «()» в этом файле.

with open("files/2538.txt") as f:
    s = f.read()

s = s.replace("()", "X")

a = []
count = 0
for i in s:
    if i == "X":
        count += 1
    else:
        a.append(count)
        count = 0

print(max(a))
