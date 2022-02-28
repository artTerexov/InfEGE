# Найдите все натуральные числа, N, принадлежащие отрезку [150 000 000; 300 000 000],
# которые можно представить в виде
# N = 2**m•3**n, где m – нечётное число, n – чётное число.
# В ответе запишите все найденные числа в порядке возрастания, а справа от каждого числа – сумму m+n.

import math


def check(numOne, numTwo, result):
    return 2 ** int(math.log(numOne, 2)) * 3 ** int(math.log(numTwo, 3)) == result or \
           2 ** int(math.log(numTwo, 2)) * 3 ** int(math.log(numOne, 3)) == result


for i in range(150000000, 300000000 + 1):
    a = set()
    for j in range(2, int(i ** 0.5) + 1):
        pass