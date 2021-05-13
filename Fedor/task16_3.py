# (№ 3986) Алгоритм вычисления значения функции F(n), где n – целое число,
# задан следующими соотношениями:
# F(0) = 0
# F(n) = F(n/2) + 3, когда n > 0 и делится на 2,
# F(n) = 2·F(n - 1) + 1, когда > 0 и не делится на 2.
# Сколько различных значений может принимать функция F(n) при n, принадлежащих отрезку [1; 1000]?

def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n // 2) + 3
    if n > 0 and n % 2 != 0:
        return 2 * F(n - 1) + 1


b = set()
for i in range(1, 1001):
    b.add(F(i))

print(len(b))