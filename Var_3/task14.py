# Значение арифметического выражения: 9^17 + 3^16 – 27 записали в системе
# счисления с основанием 3. Какая из цифр чаще всего встречается в полученном числе?
# В ответе укажите, сколько таких цифр в этой записи.

def remake(num: int, base: int) -> str:
    buff = ""
    while num // base > 0:
        buff += str(num % base)
        num = num // base
    buff += str(num)
    return buff[::-1]


n = 9 * 9 + 3 * 21 - 7
print(remake(n))