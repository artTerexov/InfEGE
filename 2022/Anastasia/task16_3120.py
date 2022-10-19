# (№ 3120) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 2·n при n < 3
# F(n) = 3·n + 5 +  F(n–2), если n ≥ 3 и чётно,
# F(n) = n + 2·F(n–6), если n ≥ 3 и нечётно.
# Чему равно значение функции F(61)?

# 3! = 1 * 2 * 3 = 6

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(20))