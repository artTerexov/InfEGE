# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим
# правилам.
# 1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее
# возможные двузначные числа (числа не могут начинаться с нуля).
# 2. На экран выводится разность полученных двузначных чисел.
# Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр –
# 53, наименьшее – 13. На экран выводится разность 53 – 13 = 40.
# Чему равно наименьшее возможное трёхзначное число N, в результате обработки
# которого на экране автомата появится число 60?


for i in range(100, 1000):
    numbers = [j for j in str(i)]
    numbers.sort()
    maximum = int(numbers[-1] + numbers[-2])
    if numbers[0] == "0":
        minumum = int(numbers[1] + numbers[0])
    else:
        minumum = int(numbers[0] + numbers[1])
    if maximum - minumum == 60:
        print(i, maximum, minumum, numbers)
        break