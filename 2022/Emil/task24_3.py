# 3. Текстовый файл 3.txt состоит не более чем из 10^6 символов.
# Определите минимальное чётное число, записанное в этом файле.


with open('3.txt') as f:
    s = f.read()

numList = [str(i) for i in range(0, 10)]

minimum = 10000000
buff = ""
for elem in s:
    if elem in numList:
        buff += elem
    elif buff != "":
        if int(buff) % 2 == 0:
            minimum = min(minimum, int(buff))
        buff = ""

print(minimum)