# Разведчик кодирует символы текста пятью стрелками.
# Каждая стрелка может иметь четыре положения (направления): ↑→↓←.
# Для первой стрелки запрещено положение вверх: ↑. Стрелки, расположенные через
# одну, не могут находиться в одинаковом положении (направлении): первая и
# третья, вторая и четвертая,
# третья и пятая. Сколько всего различных символов текста может закодировать разведчик?

import itertools

a = set(itertools.product("↑→↓←", repeat=5))
count = 0
for i in a:
    b = "".join(i)
    if b[0] != "↑" and b[0] != b[2] and b[1] != b[3] and b[2] != b[4]:
        count += 1
print(count)