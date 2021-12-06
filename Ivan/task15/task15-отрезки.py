# На числовой прямой даны два отрезка: P = [20, 50] и Q = [30, 40]. Найдите наименьшую возможную длину отрезка A, при котором формула
# ¬(x ∈ A) → ¬((x ∈ P) ∨ (x ∈ Q))
# тождественно истинна, то есть принимает значение 1 при любых x


P = [i for i in range(20, 51)]
Q = [i for i in range(30, 41)]
buff = []
for x1 in range(1, 100):
    for x2 in range(x1, 100):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(-100, 100):
            if ((not (x in A)) <= (not ((x in P) or (x in Q)))) == 0:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)
print(min(buff))