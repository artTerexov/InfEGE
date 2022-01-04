# № 1727 На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1 Строится двоичная запись числа N.
# 2 К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа).
# Например, запись 11100 преобразуется в запись 111001;б) над этой записью производятся те же действия – справа
# дописывается остаток от деления суммы цифр на 2.
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью
# искомого числа R. Сколько различных чисел, принадлежащих отрезку [210; 260], могут появиться на экране в результате
# работы автомата?
count = 0
for i in range(50, 120):
    c = bin(i)
    if c.count('1') % 2 == 0:
        c += '0'
    else:
        c += '1'
    if c.count('1') % 2 == 0:
        c += '0'
    else:
        c += '1'
    if 210 <= int(c, 2) <= 260:
        count += 1
print(count)
