# Дана программа для исполнителя Редактор:
# ПОКА нашлось(42) или нашлось(32)
#    ЕСЛИ нашлось(42)
#       ТО заменить(42, 51)
#    ИНАЧЕ заменить(32, 61)
# КОНЕЦ ПОКА
# На вход программе подана строка, содержащая только 20 двоек, 15 троек и 10 четверок.
# Порядок символов заранее неизвестен. Определите максимально возможную сумму всех цифр в конечной строке.

s = '32' * 15 + '42' * 5 + '4' * 5

while '42' in s or '32' in s:
    if '42' in s:
        s = s.replace("42", '51', 1)
    else:
        s = s.replace('32', '61', 1)

total = 0

for i in s:
    total += int(i)

print(total)