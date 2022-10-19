# 4. Текстовый файл 4.txt состоит не более чем из 10^6 символов.
# Определите самое большое число, состоящее только из нечётных цифр.


with open('4.txt') as f:
    s = f.read()

numList = [str(i) for i in range(0, 10)]

maximum = 0
buff = ""
flag = True

for elem in s:
    if elem in numList:
        buff += elem
        if int(elem) % 2 == 0:
            flag = False
    elif buff != "":
        if flag:
            maximum = max(maximum, int(buff))
        flag = True
        buff = ""

print(maximum)
