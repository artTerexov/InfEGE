# Укажите наибольшее целое значение А, при котором выражение
# (5y + 7x ≠ 129) ∨ (3x > A) ∨ (4y > A)
# истинно для любых целых положительных значений x и y.

for A in range(1000, 0, -1):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (5*y+7*x != 129) or (3*x>A) or (4*y>A)
            if F == 0:
                break
        if F == 0:
            break
    if F == 1:
        print(A)
        break

