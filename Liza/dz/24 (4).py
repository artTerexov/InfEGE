# Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 10^6 символов.
# Определите максимальное количество идущих подряд символов, среди которых не более двух точек.


with open('24-181.txt') as f:
    s = f.read().split('.')

buff = []
for i in range(len(s) - 2):
    n = len(s[i]) + len(s[i + 1]) + len(s[i + 2]) + 2
    buff.append(n)
print(max(buff))


# jgjfgjhfj.gnjdjgsdjg.gdsfgdfgdgd -> 'jgjfgjhfj', 'gnjdjgsdjg', 'gdsfgdfgdgd', 'gdsfgdfgdgd'