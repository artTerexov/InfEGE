# На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 10 цифр 1, 20 цифр 2 и 30 цифр 3, расположенных в произвольном порядке.
# Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы.
# Так, например, если результат работы программы представлял бы собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
# НАЧАЛО
# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>3)
#         ТО заменить (>3, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

s = ">" + 20 * "2" + 10 * "1" + 30 * "3"

while (">1" in s) or (">2" in s) or (">3" in s):
    if ">1" in s:
        s = s.replace(">1", "22>", 1)
    if ">2" in s:
        s = s.replace(">2", "2>", 1)
    if ">3" in s:
        s = s.replace(">3", "1>", 1)

print(s)