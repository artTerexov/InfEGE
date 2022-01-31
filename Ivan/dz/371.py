# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка
# на натуральное число m». Для какого наименьшего натурального числа А формула
# ДЕЛ(x,А) → (¬ДЕЛ(x,21) ∨ ДЕЛ(x,35))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

buff = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if ((x % A == 0) <= (not (x % 21 == 0) or (x % 35 == 0))) == 0:
            flag = False
            break
    if flag:
        buff.append(A)

print(min(buff))