# Значение арифметического выражения: 7^500 + 7^200 – 7^50 – Х записали в системе счисления с основанием 7.
# Какая максимальная сумма разрядов может быть в таком числе, при условии что X и полученное значение положительны?

# Перевод числа их 10 в base СС.
def numberTranslation(number, base):
    buff = ""
    while number:
        buff += str(number % base)
        number //= base
    return buff[::-1]


a = []
for x in range(100000, 10000000):
    n = 7 ** 500 + 7 ** 200 - 7 ** 50 - x
    n = numberTranslation(n, 7)
    summa = 0
    for i in n:
        summa += int(i)
    a.append(summa)

print(max(a))

