# В текстовом файле 4.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите максимальную длину цепочки вида
# BAFEBAFEBAFE...(состоящей из фрагментов BAFE, последний фрагмент может быть неполным).

with open('4.txt') as f:
    s = f.read()

count = 0
maxi = 0
for i in range(0, len(s)):
    if s[i] == 'B' and count % 4 == 0:
        count += 1
    elif s[i] == 'A' and count % 4 == 1:
        count += 1
    elif s[i] == 'F' and count % 4 == 2:
        count += 1
    elif s[i] == 'E' and count % 4 == 3:
        count += 1
    else:
        maxi = max(maxi, count)
        count = 0

print(max(maxi, count))