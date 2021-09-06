# F(n) = n*n + 5*n + 4, при n > 30
# F(n) = F(n+1) + 3*F(n+4), при чётных n ≤ 30
# F(n) = 2*F(n+2) + F(n+5), при нечётных n ≤ 30



# def F(n):
#     return n * n
#
# count = 0
#
# for i in range(1, 1001):
#     summa = 0
#     n = F(i)
#     # Сумма цифр числа
#     for j in str(n):
#         summa += int(j)
#     # summa хранит сумму цифр
#     if summa == 1:
#         count += 1
# print(count)






# def F(n):
#     if n > 30 :
#         return n * n + 5 * n + 4
#     if n <= 30 and n % 2 == 0:
#         return F(n +1) + 3 * F(n + 4)
#     if n <= 30 and n % 2 != 0:
#         return 2 * F(n + 2) + F(n + 5)
#
#
# count = 0
# for i in range(1, 1001):
#     summa = 0
#     n = F(i)
#     for j in str(n):
#         summa += int(j)
#     if summa == 27:
#         count += 1
# print(count)

print(3 * 5 * 5 * 5 * 5 * 3)