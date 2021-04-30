def F(n):
    return n * n

count = 0

for i in range(1, 1001):
    summa = 0
    n = F(i)
    # Сумма цифр числа
    for j in str(n):
        summa += int(j)
    # summa хранит сумму цифр
    if summa == 1:
        count += 1
print(count)