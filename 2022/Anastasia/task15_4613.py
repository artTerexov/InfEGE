# На числовой прямой даны три отрезка: P = [5, 108], Q = [28, 40] и R = [task16, 72].
# Какова наименьшая длина отрезка A, при котором формула
# ((x ∈ P) → (x ∈ Q)) ∨ (¬(x ∈ A) → ¬(x ∈ R))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

P = [i for i in range(5, 109)]
Q = [i for i in range(28, 41)]
R = [i for i in range(16, 73)]
buff = []
for x1 in range(0, 200):
    for x2 in range(x1, 200):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(1, 1000):
            if (((x in P) <= (x in Q)) or ((not (x in A)) <= (not (x in R)))) == 0:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)

print(min(buff))