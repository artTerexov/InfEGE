# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 2*n*n + 4*n + 3, при n ≤ task15
# F(n) = F(n-1) + n*n + 3, при n > task15, кратных 3
# F(n) = F(n-2) + n - 6, при n > task15, не кратных 3
# Определите количество натуральных значений n из отрезка [1; 1000], для которых все цифры значения F(n) нечётные.

def F(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n > 15 and n % 3 == 0:
        return F(n - 1) + n * n + 3
    if n > 15 and n % 3 != 0:
        return F(n - 2) + n - 6


count = 0
for i in range(1, 1001):
    m = F(i)
    k = 0
    for j in str(m):
        if int(j) % 2 != 0:
            k += 1
    if k == len(str(m)):
        count += 1
print(count)