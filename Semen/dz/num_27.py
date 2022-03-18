# Дана последовательность из N натуральных чисел. Рассматриваются все её непрерывные подпоследовательности, такие что сумма элементов каждой из них кратна k = 67.
# Найдите среди них подпоследовательность с максимальной суммой. Укажите в ответе найденную максимальную сумму.



with open("27_A (4).txt") as f:
    s = [int(i) for i in f.read().strip().split("\n")]

s.pop(0)
K = 43
ost = s[0] % K


buff = []
count = 0
for i in range(len(s)):
    count += s[i]
    if count % K == ost:
        continue
    else:
        ost = count % K
        buff.append(count - s[i])
        buff.append(count)

buff.append(count)
ost_1 = []
a = buff[0]
buff.pop(0)
for i in range(len(buff) - 1):
    if buff[i] % K == buff[i + 1] % K:
        ost_1.append(buff[i + 1] - buff[i])

print('Твой код', max(max(ost_1), a))



def F(s):
    K = 43
    total_remainder = [10 ** 10] * K
    k = [0] * K
    mx = 0
    ln = 0
    total = 0

    total_remainder[0] = 0
    k[0] = -1

    for i in range(len(s)):
        total += s[i]
        r = total % K

        if total - total_remainder[r] == mx:
            ln = min(ln, i - k[r])

        if total - total_remainder[r] > mx:
            mx = total - total_remainder[r]
            ln = i - k[r]
        if total_remainder[r] > total:
            total_remainder[r] = total
            k[r] = i

    return mx


print('Мой код', F(s))
