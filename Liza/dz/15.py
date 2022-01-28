# На числовой прямой даны два отрезка: P = [20, 30] и Q = [10, 40].
# Найдите наименьшую возможную длину отрезка A, при котором формула
# ¬((x ∈ Q) → (x ∈ A)) ∧ (x ∈ P)
#
# тождественно ложна, то есть принимает значение 0 при любых x.

P = [i for i in range(20, 30)]
Q = [i for i in range(10, 40)]
buff = []

for x1 in range(0, 150):
    for x2 in range(x1 + 1, 150):
        A = [i for i in range(x1, x2 + 1)]
        flag = 0
        for x in range(0, 150):
            if (not ((x in Q) <= (x in A)) and (x in P)) == 1:
                flag = 0
                break
        if flag:
            buff.append(x2 - x1)

print(min(buff))
