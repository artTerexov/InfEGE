# Автомат получает на вход трёхзначное число. По этому числу строится новое
# число по следующим правилам.
# 1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее
# возможные двузначные числа (числа не могут начинаться с нуля).
# 2. На экран выводится разность полученных двузначных чисел.
# Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53,
# наименьшее – 13. На экран выводится разность 53 – 13 = 40.
# Чему равно наибольшее возможное трёхзначное число N, в результате обработки которого
# на экране автомата появится число 14?


for i in range(100, 1000):
    l = [j for j in str(i)]
    l.sort()
    maximum = int(l[2] + l[1])
    if l[0] == "0":
        minimum = int(l[1] + l[0])
    else:
        minimum = int(l[0] + l[1])
    if (maximum - minimum) == 14:
        print(i)
