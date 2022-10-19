# Текстовый файл 24-164.txt состоит не более чем из 106 символов и
# содержит только заглавные буквы латинского алфавита (ABC…Z). Текст
# разбит на кстроки различной длины. Необходимо найти строку, содержащую
# самую длинную цепочку стоящих подряд одинаковых букв. Если таких строк
# несколько, надо взять ту, которая в файле встретилась раньше. Определите,
# какая буква встречается в этой строке чаще всего. Если таких букв несколько,
# надо взять ту, которая стоит раньше в алфавите. Запишите в ответе эту букву, а
# затем – сколько раз она встречается во всем файле.
# Пример. Исходный файл:
# ZZQABA
# ZALAAC
# QRAQUT
# В этом примере в первой и второй строках наибольшая длина цепочек одинаковых буквы
# равна 2 (ZZ в первой строке, AA во второй), в третьей – 1. Берём первую строку,
# т.к. она находится в файле раньше. В этой строке чаще других встречаются буквы Z и A
# (по 2 раза), выбираем букву A, т. к. она стоит раньше в алфавите. В ответе для
# этого примера надо записать A6, так как во всех строках файла буква A встречается 6 раз.

f = open("24-164.txt")
a = f.read()
s = a.split("\n")
f.close()

letter = ""
number = 0

stringNumber = -1


for string in s:
    flag = ""
    count = 1
    for i in string:
        if flag == "":
            flag = i
            continue
        if i == flag:
            count += 1
        if i != flag:
            if number < count:
                number = count
                letter = flag
                stringNumber = s.index(string)
            elif number == count and s.index(string) < stringNumber:
                letter = flag
            else:
                flag = i
                count = 1

count = 0
for i in s[stringNumber]:
    if s[stringNumber].count(i) > count or (s[stringNumber].count(i) == count and ord(i) < ord(letter)):
        count = s[stringNumber].count(i)
        letter = i

print(letter, a.count(letter), sep="")