# Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
# F(n) = n, при n ≤ 1,
# F(n) = 1 + F(n / 2), когда n > 1 и чётное,
# F(n) = 1 + F(n + 2) , когда n > 1 и нечётное.
# Назовите минимальное значение n, для которого F(n) = 16.

def F(n):
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        return 1 + F(n // 2)
    if n > 1 and n % 2 != 0:
        return 1 + F(n + 2)


for i in range(1, 100000):
    try:
        if F(i) == 16:
            print(i)
            break
    except RecursionError:
        continue
