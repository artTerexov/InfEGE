# (№ 3515) (Е. Джобс) Значение арифметического выражения 43∙7103 – 21∙757 + 98 записали в системе счисления с основанием 7.
# Найдите сумму разрядов получившегося числа и запишите её в ответе в десятичной системе счисления.
num = 43 * 7 ** 103 - 21 * 7 ** 57 + 98
base = 7

buff = ''
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]

s = 0

# for i in range(len(buff)):
#     s += int(buff[i])

for i in buff:
    s += int(i)
print(s)
