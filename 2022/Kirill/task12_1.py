# НАЧАЛО
#   ПОКА нашлось (222)
#     заменить (22, 7)
#     заменить (77, 2)
#   КОНЕЦ ПОКА
# КОНЕЦ

s = "2" * 103

while s.find("222") != -1:
    s = s.replace("22", "7", 1)
    s = s.replace("77", "2", 1)
print(s)