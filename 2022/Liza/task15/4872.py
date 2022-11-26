# (№ 4872) Элементами множеств А, P и Q являются натуральные числа, причём P = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20} и Q = { 5, 10, task15, 20, 25, 30, 35, 40, 45, 50}. Известно, что выражение
# ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
#
# истинно (т. е. принимает значение 1) при любом значении переменной х. Определите наибольшее возможное количество элементов множества A.


P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}


A_1 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
A_2 = {2, 4, 6, 8, 12, 14, 16, 18}
A_3 = {5, 15, 25, 30, 35, 40, 45, 50}
A_4 = {20, 10}

for A in A_1, A_2, A_3, A_4, P, Q:
    flag = 1
    for x in range(-100, 100):
        if ((x not in A or x in P) and (x not in Q or x not in A)) == 0:
            flag = 0
            break
    if flag:
        print(A)