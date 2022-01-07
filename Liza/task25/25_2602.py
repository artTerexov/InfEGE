# Среди целых чисел, принадлежащих числовому отрезку[412567; 473265], найдите числа,
# которые представляют собой произведение двух различных простых делителей.
# Запишите в ответе количество таких чисел и то из их, которое ближе всего к их среднему арифметическому.

def checkSimple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


count = []
for l in range(412567, 473266):
    for k in range(2, int(l ** 0.5) + 1):
        if l % k == 0 and k != l // k:
            if checkSimple(k) and checkSimple(l // k):
                count.append(l)
                break
print(len(count))

