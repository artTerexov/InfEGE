# Обозначим через P(N) – произведение 5 наименьших различных нетривиальных
# делителей натурального числа N (не считая единицы и самого числа).
# Если у числа N меньше 5 таких делителей, то P(N) считается равным нулю.
# Найдите 5 наименьших натуральных чисел, превышающих 500 000 000, для которых
# P(N) оканчивается на 91 и не превышает N. В ответе для каждого найденного
# числа запишите сначала значение P(N), а затем – наибольший делитель, вошедший в произведение P(N).

def P(n):
    buff = []
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            buff.append(j)
            if j != n // j:
                buff.append(n // j)
    if len(buff) < 5:
        return 0
    buff.sort()
    result = 1
    for i in range(0, 5):
        result *= buff[i]
    if str(result)[-2::] == "91" and result <= n:
        print(result, buff[4])


for m in range(500000000, 500000000 * 10):
    P(m)
