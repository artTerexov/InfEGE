# Для какого наибольшего целого неотрицательного числа А выражение
# (x2 – 11x + 28 > 0) ∨ (y2 – 9y + 14 > 0) ∨ (x2 + y2 > A)
# тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y?

for A in range(0, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x ** 2 - 11 * x + 28 > 0) or (y ** 2 - 9 * y + 14 > 0) or (x ** 2 + y ** 2 > A)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
