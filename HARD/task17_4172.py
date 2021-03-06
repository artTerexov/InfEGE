# Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
# F(n) = n + 3, при n ≤ 3
# F(n) = F(n – 2) + n, при n > 3 и четном значении F(n-1),
# F(n) = F(n – 2) + 2•n, при n > 3 и нечетном значении F(n-1).
# Определите сумму значений, являющихся результатом вызова функции для значений
# n в диапазоне [40; 50].

from functools import lru_cache


@lru_cache()
def F(n):
    if n <= 3:
        return n + 3
    else:
        t1 = F(n - 1)
        t2 = F(n - 2)
        if t1 % 2 == 0:
            return t2 + n
        else:
            return t2 + 2 * n

sum = 0
for i in range(40, 51):
    sum += F(i)
print(sum)
