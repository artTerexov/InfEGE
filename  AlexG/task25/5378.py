# Среди натуральных чисел, не превышающих 108, найдите все числа, соответствующие маске 12*4?65,
# делящиеся на 161 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в
# порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 161.

# * - нет символов
for j in range(10):
    num = int('12' + '4' + str(j) + '65')
    if num % 161 == 0:
        print(num, num // 161)

# * - 1 символ
for i in range(10):
    for j in range(10):
        num = int('12' + str(i) + '4' + str(j) + '65')
        if num % 161 == 0:
            print(num, num // 161)

# * - 2 символ
for i in range(10):
    for k in range(10):
        for j in range(10):
            num = int('12' + str(i) + str(k) + '4' + str(j) + '65')
            if num % 161 == 0:
                print(num, num // 161)


# 1234065 7665
# 12004965 74565
# 12214265 75865
# 12294765 76365
# 12504065 77665
# 12584565 78165
# 12874365 79965
# 12954865 80465


# 1234065 7665
# 12004965 74565
# 12214265 75865
# 12294765 76365
# 12504065 77665
# 12584565 78165
# 12874365 79965
# 12954865 80465