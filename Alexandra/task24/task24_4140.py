# (№ 4140) (А. Богданов) Текстовый файл 24-169.txt состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки символов, состоящей из повторяющихся фрагментов XYZ.
# Цепочка может начинаться и заканчиваться любым символом из XYZ, но внутри цепочки порядок строго
# определен. Например, для строки ZZZXYZXYZXZZZ длина цепочки равна 8: Z+XYZ+XYZ+X, где цепочка
# начинается с Z и заканчивается X.


with open('files/24-169.txt') as f:
    a = f.read().strip()


count = 0
m_count = 0
a = a.replace('XYZ', '.')

for i in range(1, len(a) - 1):
    if a[i] == '.':
        count += 3
        if a[i - 1] == 'Z':
            count += 1
        if a[i + 1] == 'X':
            count += 1
    else:
        m_count = max(m_count, count)
        if m_count == 69:
            print(a[i - 70: i + 1])
            break
        if a[i] == 'Z':
            count = 1
        else:
            count = 0

print(m_count)