# Перевод из 10 в 2 сс
num = bin(41)[2:]
print(num)
# 1. bin - возвращает строковое значение - это значит, что никакой математики. но можем обращаться по индексам к элементам
# 2. Мы должны избавиться от префикса '0b' с помощью СРЕЗА. num = bin(6)[2:]

# Перевод из 10 в 8
num = oct(41)[2:]
print(num)
# Перевод из 10 в 16
num = hex(41)[2:]
print(num)
# Перевод из ЛЮБОЙ в 10ую сс
num = int('10000', 2)
print(num)
