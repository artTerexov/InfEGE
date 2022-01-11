# 	(№ 3813) Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
# F(n) = 1, при n < 2,
# F(n) = F(n/2) + 1, когда n ≥ 2 и чётное,
# F(n) = F(n - 3) + 3, когда n ≥ 2 и нечётное.
# Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 12.
def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return F(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(n - 3) + 3


count = 0
for i in range(1, 100001):
    try:
        if F(i) == 12:
            count += 1
    except RecursionError:
        continue

print(count)
