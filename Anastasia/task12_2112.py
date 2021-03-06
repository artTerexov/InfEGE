# (№ 2112) (А. Кабанов) Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
# 1. заменить (v, w)
# 2. нашлось (v)
# Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w, вторая проверяет, встречается ли цепочка v в строке исполнителя Редактор. Если она встречается, то команда возвращает логическое значение «истина», в противном случае возвращает значение «ложь».
# К исходной строке, содержащей не более 100 единиц и не содержащей других символов, применили приведённую ниже программу.
# НАЧАЛО
#   ПОКА нашлось (111)
#     заменить (111, 2)
#     заменить (222, 3)
#     заменить (333, 1)
#   КОНЕЦ ПОКА
# КОНЕЦ
# В результате получилась строка 321. Сколько различных значений количества единиц может быть в исходной строке?

count = 0
for i in range(1, 100):
    s = '1' * i

    while '111' in s:
        if '111' in s:
            s = s.replace('111', '2', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
        if '333' in s:
            s = s.replace('333', '1', 1)
    if s == "321":
        count += 1

print(count)
