# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан
# следующими соотношениями:
#       F(n) = n + 3, при n ≤ 18
#       F(n) = (n//3)*F(n//3) + n - 12, при n > 18, кратных 3
#       F(n) = F(n-1) + n*n + 5, при n > 18, не кратных 3
# Здесь // обозначает деление нацело. Определите количество натуральных значений n из
# отрезка [1; 800], для которых все цифры значения F(n) чётные.

def F(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n // 3) * F(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return F(n - 1) + n * n + 5


count = 0
flag = 0

for i in range(1, 801):
    s = str(F(i))
    for j in s:
        if int(j) % 2 != 0:
            flag = -1
            break
    if flag != -1:
        count += 1
    flag = 0

print(count)
