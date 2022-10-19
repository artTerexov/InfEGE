# (№ 3485) (А.М. Кабанов) Для какого наименьшего целого неотрицательного числа А выражение
# (x2 – 10x + task16 > 0) ∨ (y2 – 10y + 21 > 0) ∨ (xy < 2A)
# тождественно истинно, т.е. принимает значение 1 при любых целых положительных x и y?


for A in range(0, 1001):
    flag = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (((x ** 2 - 10 * x + 16) > 0) or ((y ** 2 - 10 * y + 21) > 0) or ((x * y) < (2 * A))) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
