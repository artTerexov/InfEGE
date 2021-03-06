# 2) Подсчитывается количество нулей и единиц в полученной записи. Если их количество одинаково,
#  в конец записи добавляется её последняя цифра. В противном случае в конец записи добавляется цифра,
#  которая встречается реже.
# 3) Шаг 2 повторяется ещё два раза.
# 4) Результат переводится в десятичную систему счисления.
# При каком наименьшем исходном числе N > 90 в результате работы алгоритма получится чётное число, которое не делится на 4?


for N in range(91, 1000):
    n = bin(N)[2:]
    for i in range(3):
        if n.count('0') == n.count('1'):
            n += n[-1]
        elif n.count('0') > n.count('1'):
            n += '1'
        elif n.count('0') < n.count('1'):
            n += '0'
    if int(n, 2) % 2 == 0 and int(n, 2) % 4 != 0:
        print(N)
        break