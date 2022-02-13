# На вход программе подается последовательность чисел, а также натуральные числа K и D. Особыми называются отрицательные
# числа, для которых сумма цифр троичной записи равна 12. Рассматриваются все непрерывные подпоследовательности исходной
# последовательности, в которых количество особых чисел кратно K, а количество всех элементов подпоследовательности
# кратно D. Программа должна вывести одно число – максимальную сумму такой последовательности.
with open('27_tasks/27-91a.txt') as f:
    a = f.read().strip().split('\n')

with open('27_tasks/27-91b.txt') as f:
    b = f.read().strip().split('\n')


def check(a):
    if a < 0:
        s = -a
        s1 = ''
        while s:
            s1 = str(s % 3) + s1
            s //= 3
        count = 0
        for i in range(len(s1)):
            count += int(s1[i])
        return count


def F(a):
    k_unique = int(a[0].split()[1])
    d_amount = int(a[0].split()[2])
    count_u = 0
    count_amount = 0
    total_rem = [10965946660000] * d_amount
    k = [0] * d_amount
    mx = 0
    a.pop(0)
    for i in range(len(a)):
        count_amount += int(a[i])
        if check(int(a[i])) == 12:
            count_u += 1
        r = count_u % k_unique

        if count_amount - total_rem[r] > mx and (i - k[r]) % d_amount == 0:
            mx = count_amount - total_rem[r]
        if total_rem[r] > count_amount:
            total_rem[r] = count_amount
            k[r] = i
    return mx

print(F(a), F(b))
