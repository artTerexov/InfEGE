# Для интервала [33333;55555] найти все простые числа, сумма цифр которых больше 35.
# Запишите найденные числа в порядке возрастания, справа от каждого – сумму его цифр.


def prime(l):
    buff = []
    for k in range(2, int(l ** 0.5 + 1)):
        if l % k == 0:
            buff.append(k)
    if len(buff) != 0:
        return False
    else:
        return True

for i in range(33333, 55555 + 1):
    length = 0
    for n in range(len(str(i))):
        length += int(str(i)[n])
    if length > 35 and prime(i):
        print(i, length)