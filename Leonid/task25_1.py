# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [174457; 174505], числа, имеющие ровно два различных натуральных делителя,
# не считая единицы и самого числа. Для каждого найденного числа запишите эти
# два делителя в таблицу на экране с новой строки в порядке возрастания произведения
# этих двух делителей. Делители в строке таблицы также должны следовать в порядке возрастания.

buff = []

for i in range(174457, 174506):
    if len(buff) == 2:
        print(buff)
        buff.clear()
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            buff.append(j)
            if len(buff) > 2:
                buff.clear()
                break
