# На числовой прямой даны два отрезка: P = [20, 30] и Q = [35, 60]. Найдите
# наименьшую возможную длину отрезка A, при котором формула
# ¬(x ∈ A) ∧ ((x ∈ P) ∨ (x ∈ Q))
# тождественно ложна, то есть принимает значение 0 при любых x.


P = [i for i in range(20, 31)]
Q = [i for i in range(35, 61)]
buff = []

for x1 in range(20, 61):
    for x2 in range(x1, 61):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(-100, 100):
            if ((not (x in A)) and ((x in P) or (x in Q))) == 1:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)

print(min(buff))