# Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 10^6
# символов. Определите максимальное количество идущих подряд символов, среди которых не более трёх точек.

# A...AAA.AAA.AAAA.AAAAA.SAFFASF

with open('4526.txt') as f:
    s = f.read()

a = s.split('.')
result = 0
for i in range(len(a) - 3):
    if len(a[i]) + len(a[i + 1]) + len(a[i + 2]) + len(a[i + 3]) + 3 > result:
        result = len(a[i]) + len(a[i + 1]) + len(a[i + 2]) + len(a[i + 3]) + 3

print(result)



