with open("27_test") as f:
    s = f.read().split()[1:]


def get_sum(index, distance, arr):
    ln = len(arr)
    num1 = index - distance
    num2 = index + distance

    if distance == len(arr) // 2:
        return
    if num2 > ln:
        num2 = num2 - ln



    return [num1, num2]


s = [int(i) for i in s]
print(s)

min_summa = 9999
needed_point = 0
# Место завода
for i in range(0, len(s)):
    summa = 0
    # Расстояние
    for k in range(0, len(s) // 2 + 1):
        t = get_diff(i, k, s)
        summa += s[t[0]] * k + s[t[1]-1] * k

    if summa < min_summa:
        min_summa = summa
        needed_point = i


print(min_summa, needed_point)