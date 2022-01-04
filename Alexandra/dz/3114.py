#  Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# # F(n) = n при n > 15
# # F(n) = 2·F(n+1) + 5·n + 2, если n ≤ 15
# # Чему равно значение функции F(2)?

def F(n):
    if n > 15:
        return n
    if n <= 15:
        return 2 * F(n + 1) + 5 * n + 2
print(F(2))