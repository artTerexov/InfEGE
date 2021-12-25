# ((¬ДЕЛ(x, A) ∧ ДЕЛ(x, 180)) → ДЕЛ(x, 130)) ∧ (A < 100)

buff = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (((not x % A == 0) and (x % 180 == 0)) <= (x % 130 == 0) and (A < 100)) == 0:
            flag = False
            break
    if flag:
        buff.append(A)

print(max(buff))