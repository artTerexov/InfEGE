# В текстовом файле k8.txt находится цепочка из не более чем 106 символов,
# в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры. Найдите длину самой длинной подцепочки,
# состоящей из одинаковых символов. Выведите сначала символ, из которого строится цепочка, а затем через пробел – длину этой цепочки
# . Если таких цепочек (максимальной длины) несколько, выведите информацию о первой встретившейся цепочке.
with open('files/2507.txt') as f:
    s = f.read()
symbol_max = ''
count = 0
count_max = 0
symbol = s[0]
for i in s:
    if i == symbol:
        count += 1
    else:
        if count > count_max:
            count_max = count
            symbol_max = symbol
        count = 1
        symbol = i
print(symbol_max, count_max)