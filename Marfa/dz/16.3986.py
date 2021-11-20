# F(0) = 0
# F(n) = F(n/2) + 3, при чётном n > 0
# F(n) = 2·F(n - 1) + 1, при нечётном n > 0
# Сколько различных значений может принимать функция F(n) при n, принадлежащих отрезку [1; 1000]?

def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) + 3
    if n > 0 and n % 2 != 0:
        return 2 * f(n - 1) + 1


a = set()
for i in range(1, 1001):
    a.add(f(i))
print(len(a))