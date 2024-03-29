# (№ 3434) Элементами множеств А, P и Q являются натуральные числа,
# причём P={2, 4, 6, 8, 10, 12, 14, task16, 18, 20} и
# Q={5, 10, task15, 20, 25, 30, 35, 40, 45, 50}. Известно, что выражение
# ((x ∈A) → (x ∈P)) ∨ (¬(x ∈Q) → ¬(x ∈A))
# истинно (т.е. принимает значение 1 при любом значении переменной х.
# Определите наибольшее возможное количество элементов в множестве A.

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

for A in P & Q, P | Q, P ^ Q, Q ^ P:
    flag = True
    for x in range(-1000, 1000):
        if (((x in A) <= (x in P)) or ((x not in Q) <= (x not in A))) == 0:
            flag = False
            break
    if flag:
        print(len(A))