# Значение арифметического выражения: 9^7 + 3^21 – 8 записали в системе счисления
# с основанием 3. Найдите сумму цифр в этой записи. Ответ запишите в десятичной системе.

n = 9 ** 7 + 3 ** 21 - 8

number = ""

while n // 3 != 0:
    number += str(n % 3)
    n = n // 3
number += str(n)
number = number[::-1]

result = 0
for i in number:
    result += int(i)

print(result)

