# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1) Строится двоичная запись числа N.
# 2) Подсчитывается количество нулей и единиц в полученной записи. Если их количество одинаково, в конец записи добавляется её последняя цифра. В противном случае в конец записи добавляется цифра, которая встречается реже.
# 3) Шаг 2 повторяется ещё два раза.
# 4) Результат переводится в десятичную систему счисления.
# При каком наибольшем исходном числе N < 100 в результате работы алгоритма получится число, которое делится на 4 и не делится на 8?

for i in range(99, 0, -1):
    n = str(bin(i))[2::]
    for j in range(4):
        if n.count("0") == n.count("1"):
            n += n[-1]
        elif n.count("0") > n.count("1"):
            n += "1"
        elif n.count("0") < n.count("1"):
            n += "0"
    if int(n, 2) % 4 == 0 and int(n, 2) % 8 != 0:
        print(i)
