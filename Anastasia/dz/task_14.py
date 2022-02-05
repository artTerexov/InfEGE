# (№ 2913) (А.Н. Носкин) Сколько различных цифр в восьмеричной записи числа 2^102 + 2^100 + 2^85 + 2^17?
num = 2 ** 102 + 2 ** 100 + 2 ** 85 + 2 ** 17
base = 8
buff = ''
while num > 0:
    buff += str(num % base)
    num = num // base
buff = buff[::-1]
count = 0
print(buff)
for i in '01234567':
    if buff.count(i) != 0:
        count += 1
print(count)
