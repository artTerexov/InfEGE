# (№ 4605) На числовой прямой даны два отрезка: P = [15, 75] и Q = [30, 75].
# Найдите наименьшую возможную длину отрезка A, при котором формула
# (¬(x ∈ P) ∨ (x ∈ Q)) → ¬(x ∈ A)
#
# тождественно истинна, то есть принимает значение 1 при любых x.

P = [i for i in range(15, 76)]
Q = [i for i in range(30, 76)]
buff = []
for x1 in range(1, 100):
    for x2 in range(x1, 100):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(1, 1000):
            if (((not (x in P)) or (x in Q)) <= (not (x in A))) == 0:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)

print(min(buff))