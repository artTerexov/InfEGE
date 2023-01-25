# Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
# которые представляют собой произведение трёх различных простых делителей, оканчивающихся
# на одну и ту же цифру. В ответе запишите количество таких чисел и такое из них,
# для которого разность наибольшего и наименьшего простых делителей минимальна.


def is_simple(n: int) -> bool:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


count = 0
for num in range(485617, 529678 + 1):
    buff = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_simple(i):
                buff.append(i)
            if is_simple(num // i):
                buff.append(num // i)

    if len(buff) == 3 and str(buff[0])[-1] == str(buff[1])[-1] == str(buff[2])[-1] and buff[0] * buff[1] * buff[2] == num:
        # print(num)
        count += 1
print(count)
