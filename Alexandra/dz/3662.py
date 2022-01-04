# (№ 3662)
# Число
# 188
# записали
# в
# системах
# счисления
# с
# основаниями
# от
# 2
# до
# 10
# включительно.При
# каких
# основаниях
# цифры
# в
# записи
# этого
# числа
# расположены
# в
# порядке
# неубывания? В
# ответе
# укажите
# сумму
# всех
# подходящих
# оснований.


s1 = 188
for i in range(2, 10):
    s = 188
    c = ''
    while s:
        c = str(s % i) + c
        s //= i
    print(i, c)
print('Ответ: 31')