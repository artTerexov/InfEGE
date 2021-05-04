# https://inf-ege.sdamgia.ru/problem?id=15924
# НАЧАЛО
#     ПОКА нашлось (1111)
#         заменить (1111, 22)
#         заменить (222, 1)
#     КОНЕЦ ПОКА
# КОНЕЦ

s = "1" * 101

while "1111" in s:
    s = s.replace("1111", "22", 1)
    s = s.replace("222", "1", 1)

print(s)
