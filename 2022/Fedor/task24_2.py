# Текстовый файл 24.txt состоит не более чем из 10^6 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.

"XXYZYXZYXXYZ"

with open("24.txt") as f:
    s = f.read()
count = 0
m = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
    else:
        m = max(m, count)
        count = 0
print(m)
