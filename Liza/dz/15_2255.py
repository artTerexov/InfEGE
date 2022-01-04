# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
# (ДЕЛ(x, A) ∧ ДЕЛ(x, 21)) → ДЕЛ(x, 18)
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

def div(a, b):
    return a % b == 0


for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if ((div(x, A) and div(x, 21)) <= div(x, 18)) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)
        break