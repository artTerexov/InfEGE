# Рассматриваются возрастающие последовательности из 5 идущих подряд чисел, больших 700000, такие, что количество
# делителей каждого следующего числа превосходит количество делителей предыдущего числа. Найдите такую последовательность,
# которая начинается с наименьшего возможного числа.
# Для каждого числа из этой последовательности запишите сначала само число, а затем количество его натуральных
# делителей.

def dell(num):
    buff = [1, num]
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            buff.append(d)
            if not (num // d in buff):
                buff.append(i // d)
    return buff


for i in range(700000, 1000000):
    buffMain = []
    for j in range(i, i + 4):
        buffOne = dell(j)
        buffTwo = dell(j + 1)
        if len(buffTwo) > len(buffOne):
            buffMain.append(buffOne)
        else:
            break
        if len(buffMain) == 4:
            buffMain.append(buffTwo)
    if len(buffMain) == 5:
        for n in buffMain:
            print(max(n), len(n))
        break
