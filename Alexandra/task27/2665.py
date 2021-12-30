# Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число
# так, чтобы сумма всех выбранных чисел делилась на 5 и при этом была минимально возможной. Гарантируется, что искомую
# сумму получить можно. Программа должна напечатать одно число – максимально возможную сумму, соответствующую условиям
# задачи.
with open('files/27-5a.txt') as f:
    a = f.read().strip().split('\n')

with open('files/27-5b.txt') as f:
    b = f.read().strip().split('\n')

a.pop(0)
b.pop(0)
summa = 0
diff = []


for i in a:
    num1 = int(i.split()[0])
    num2 = int(i.split()[1])
    summa += min(num1, num2)
    diff.append(abs(num1 - num2))
diff.sort()

if summa % 5 != 0:
    for j in diff:
        if (summa + j) % 5 == 0:
            print(summa + j)
            break
else:
    print(summa)

summa = 0
diff = []

for i in b:
    num1 = int(i.split()[0])
    num2 = int(i.split()[1])
    summa += min(num1, num2)
    diff.append(abs(num1 - num2))
diff.sort()

if summa % 5 != 0:
    for j in diff:
        if (summa + j) % 5 == 0:
            print(summa + j)
            break
else:
    print(summa)