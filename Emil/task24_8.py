# В текстовом файле 2.txt находится цепочка из символов латинского алфавита
# A, B, C, D, E, F. Найдите максимальную длину цепочки вида CACACA....
# (состоящей из фрагментов CA, последний фрагмент может быть неполным).
# Выполнено на 0 баллов из 1

with open('2.txt') as f:
    s = f.read()

count = 0
maxi = 0
for i in s:
    if (i == 'C' and count % 2 == 0) or (i == 'A' and count % 2 == 1):
        count += 1
    else:
        maxi = max(maxi, count)
        if i == "C":
            count = 1
        else:
            count = 0

print(max(maxi, count))
