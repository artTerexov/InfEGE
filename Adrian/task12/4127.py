# Дана программа для исполнителя Редактор:
# ПОКА нашлось(43) ИЛИ нашлось(53)
#   ЕСЛИ нашлось(43)
#     ТО заменить(43, 33)
#     ИНАЧЕ заменить(53, 433)
# КОНЕЦ ПОКА
# Определите максимально возможное количество цифр 3, которое может получиться в результате
# применения этой программы к строке, состоящей из 17 цифр 3, 23 цифр 4 и 29 цифр 5, идущих в произвольном порядке.

s = '5' + '44553' * 11 + '453' * 1 + '53' * 5

while '43' in s or '53' in s:
    if '43' in s:
        s = s.replace('43', '33', 1)
    else:
        s = s.replace('53', '433', 1)

print(s.count('3'))
print(s)


# 53 -> 433 -> 333
# 453 -> 4433 -> 4333 -> 3333

