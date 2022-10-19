# На числовой прямой даны три отрезка: P=[10,25], Q=[15,30] и R=[25,40].
# Какова максимальная длина отрезка A, при котором формула
# ((x ∈ Q) → (x ∉ R) ) ∧ (x ∈ A) ∧ (x ∉ P)
# тождественно ложна, то есть принимает значение 0 при любом значении переменной х?

l = list()
for x1 in range(1, 100):
    for x2 in range(x1 + 1, 100):
        flag = True
        for X in range(1, 1000):
            if not((not(15 <= X <= 30) or not(25 <= X <= 40)) and (x1 <= X <= x2) and not(10 <= X <= 25)):
                continue
            else:
                flag = False
                break
        if flag:
            l.append(x2 - x1)

print(max(l))



