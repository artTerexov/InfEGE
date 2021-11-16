# Для какого наименьшего целого неотрицательного числа А выражение
# (5x – 6y < A) ∨ (x – y > 30)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y

for A in range(0, 1000):
    flag = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (5 * x - 6 * y < A or (x - y > 30)) == 0:
                flag = 0
                break
        if not flag:
            break
    if flag:
        print(A)
        break