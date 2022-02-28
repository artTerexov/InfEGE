# Дана последовательность натуральных чисел. Рассматриваются все её непрерывные последовательности, такие что сумма
# элементов каждой из них кратна K = 37, а сумма первого и последнего элемента последовательности кратна M = 73. Найдите
# среди них подпоследовательность с максимальной суммой и определите её длину. Если таких подпоследовательностей найдено
# несколько, в ответе укажите количество элементов самой короткой из них.
with open('27-78b.txt') as f:
    a = [int(i) for i in f.read().strip().split('\n')]

a.pop(0)
K = 37
M = 73
total_rem = [[10 ** 10] * K for i in range(M)]
k = [[0] * K for i in range(M)]
mx = 0
ln = 0
count_amount = 0
r = 0
for i in range(len(a)):
    count_amount += a[i]
    ri = a[i] % M
    if total_rem[ri][r] > count_amount:
        total_rem[ri][r] = count_amount - a[i]
        k[ri][r] = i
    r0 = (M - ri) % M
    r = count_amount % K
    if count_amount - total_rem[r0][r] == mx:
        ln = min(ln, i - k[r0][r] + 1)
    if count_amount - total_rem[r0][r] > mx:
        mx = count_amount - total_rem[r0][r]
        ln = i - k[r0][r] + 1
        print(mx, ln)
print(ln)