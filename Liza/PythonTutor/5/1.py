# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы
# выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами,
# то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через
# один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.


# a = input()
# print(a[2])
# print(a[-2])
# print(a[0:6])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))

a = "12345678"
count = 0

for i in a:
    if int(i) % 2 == 0:
        count += 1
print(count)