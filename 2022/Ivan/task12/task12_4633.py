# Дана программа для исполнителя Редактор:
# ПОКА нашлось (555) ИЛИ нашлось (888)
#   заменить (555, 8)
#   заменить (888, 55)
# КОНЕЦ ПОКА
# Известно, что начальная строка состоит не менее, чем из двух цифр 8 и не содержит других цифр.
# Сколько различных строк может получиться в результате работы алгоритма?

buff = set()
for i in range(2, 100):
    s = "8" * i
    while ("555" in s) or ("888" in s):
        s = s.replace("555", "8", 1)
        s = s.replace("888", "55", 1)
    buff.add(s)

print(len(buff))

