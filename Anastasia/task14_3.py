# Значение выражения 2166 + 2164 + 366 − 614 − 24 записали в системе
# счисления с основанием 6. Сколько различных цифр содержит эта запись?

num = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
base = 6
buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]


count = 0
for i in "012345":
    if buff.count(i) != 0:
        count += 1
print(count)
print(buff)