# Укажите наименьшее целое значение А, при котором выражение
# (7y + x < A) ∨ (2x + 3y > 98)
# истинно для любых целых положительных значений x и y.

for A in range(1, 10000):
    flag = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((7 * y + x) < A) or ((2 * x + 3 * y) > 98)) == 0:
                flag = 0
                break
        if not flag:
            break
    if flag:
        print(A)
        break
