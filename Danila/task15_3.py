# (С. Скопинцева) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без
# остатка на натуральное число m». Для какого наибольшего натурального числа А формула
# ¬(ДЕЛ(x, 16) ≡ ДЕЛ(x, 24)) → ДЕЛ(x, A)
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

for A in range(1, 1000):
    for x in range(1, 1000):
        F = ((x % 16 == 0) == (x % 24 == 0)) or (x % A == 0)
        if F == 0:
            break
    if F == 1:
        print(A)