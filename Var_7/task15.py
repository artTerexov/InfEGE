# (№ 2254) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа А формула
# ДЕЛ(x, A) → (¬ДЕЛ(x, 28) ∨ ДЕЛ(x, 42))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

for A in range(1, 1000):
    for x in range(1, 1000):
        F = not(x % A == 0) or (not(x % 28 == 0) or (x % 42 == 0))
        if F == 0:
            break
    if F == 1:
        print(A)
        break