# Значение выражения 11•task15^65 + 18•task15^38 – 14•task15^17 + 19•task15^11 + 18338
# записали в системе счисления с основанием task15.
# Сколько различных цифр содержится в этой записи?


def numberTranslation(number, base):
    buff = ""
    letters = "ABCDEFG"
    while number:
        if number % base > 9:
            buff += letters[number % base % 10]
        else:
            buff += str(number % base)
        number //= base
    return buff[::-1]


num = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338

result = numberTranslation(num, 15)

unique = set()
for i in result:
    unique.add(i)
print(len(unique))

print(result)



