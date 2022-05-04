# На вход программе подается последовательность чисел и значение K. Особыми называются простые числа, перед которыми стоит знак «минус».
# Рассматриваются все непрерывные подпоследовательности исходной последовательности, в которых количество особых чисел кратно K.
# Программа должна вывести одно число – максимальную сумму такой последовательности


with open("test.txt") as f:
    s = [int(i) for i in f.read().strip().split()]

# 11527919 168873874


def isPrime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False

    return True


s.pop(0)
K = s[0]
s.pop(0)

sum_ost = [100000000] * K
sum_ost[0] = 0
maximum = 0
count = 0
count_1 = 0

for i in s:
    count += i

    if i < 0 and isPrime(i):
        count_1 += 1

    ost = count_1 % K

    if sum_ost[ost] > count:
        sum_ost[ost] = count

    if count - sum_ost[ost] > maximum:
        maximum = count - sum_ost[ost]

print(maximum)

# 11527919 168873874

