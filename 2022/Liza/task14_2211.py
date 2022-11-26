# (№ 2211) (С.С. Поляков) Значение выражения (729^41 – 81^task16)∙(729^task15 + 9^5) записали в
# системе счисления с основанием 9. Сколько цифр 0 содержится в этой записи?

num = (729 ** 41 - 81 ** 16) * (729 ** 15 + 9 ** 5)
base = 9
buff = ""

while num != 0:
    buff += str(num % base)
    num //= base
buff = buff[::-1]


print(buff.count("0"))