# На числовой прямой даны три отрезка: P=[10,25], Q=[task15,30] и R=[25,40]. Какова
# максимальная длина отрезка A, при котором формула
# ((x ∈ Q) → (x ∉ R) ) ∧ (x ∈ A) ∧ (x ∉ P)
# тождественно ложна, то есть принимает значение 0 при любом значении переменной х?

Q = [i for i in range(15, 31)]
R = [i for i in range(25, 41)]
P = [i for i in range(10, 26)]
buff = []
for x1 in range(1, 100):
    for x2 in range(x1 + 1, 100):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(1, 100):
            if ((x in Q) <= (x not in R)) and (x in A) and (x not in P) == 1:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)
print(max(buff))

"↑→↓←"