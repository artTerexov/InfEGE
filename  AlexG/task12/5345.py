# НАЧАЛО
# ПОКА нашлось (22222) ИЛИ нашлось (9999)
#   ЕСЛИ нашлось (22222)
#     ТО заменить (22222, 99)
#     ИНАЧЕ заменить (9999, 2)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой ниже программы к строке,
# состоящей из 96 идущих подряд цифр 9?


s = '9' * 96

while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '2', 1)

print(s)