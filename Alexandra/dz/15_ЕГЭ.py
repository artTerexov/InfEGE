# (№ 1046) Укажите наименьшее целое значение А, при котором выражение
# (3y + x < A) ∨ (x > 12) ∨ (y > 15) истинно для любых целых положительных значений x и y.
for A in range(1, 1000):
    B = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((3*y + x < A) or (x > 12) or (y > 15)) == 0:
                B = False
                break
        if not B:
            break
    if B:
        print(A)
        break