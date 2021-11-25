# На числовой прямой даны три отрезка: P = [5, 110], Q = [15, 42] и R = [25, 70]. Какова наименьшая длина отрезка A, при котором формула
# ((x ∈ P) → (x ∈ Q)) ∨ (¬(x ∈ A) → ¬(x ∈ R))
#
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х?

P = [i for i in range(5, 111)]
Q = [i for i in range(15, 43)]
R = [i for i in range(25, 71)]

# for x1 in range(1, 200):
#     for x2 in range(x1 + 1, 200):
#         A = [i for i in range(x1, x2 + 1)]
#         flag = True
#         for x in range(1, 1000):
#             if ((x in P) <= (x in Q)) or ((x not in A) <= (x not in R)) == 0:
#                 flag = False
#                 break
#         if flag:
#             print(x2 - x1)
#             break

l = list()
for x1 in range(1, 200):
    for x2 in range(x1 + 1, 200):
        flag = True
        for X in range(1, 1000):
            if ((5 <= X <= 110) <= (15 <= X <= 42)) or ((not (x1 <= X <= x2)) <= (not(25 <= X <= 70))):
                continue
            else:
                flag = False
                break
        if flag:
            l.append(x2 - x1 + 1)

print(min(l))
