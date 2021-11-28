# Е. Джобс) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = n + 1 при n < 3
# F(n) = n + 2·F(n+2), если n ≥ 3 и чётно,
# F(n) = F(n–2) + n - 2, если n ≥ 3 и нечётно.
# Сколько существует чисел n, для которых значение F(n) определено и будет трехзначным?

def F(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return n + 2 * F(n + 2)
    if n >= 3 and n % 2 != 0:
        return F(n - 2) + n - 2


a = []
for i in range(1, 10000):
    try:
        if len(str(F(i))) == 3:
            a.append(i)
    except RecursionError:
        continue

print(len(a))