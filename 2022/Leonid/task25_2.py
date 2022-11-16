# Напишите программу, которая ищет среди целых чисел, принадлежащих
# числовому отрезку [338472; 338494], числа, имеющие ровно 4 различных делителя.
# В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.

buff = []

for i in range(338472, 338495):
    if len(buff) == 4:
        print(sorted(buff))
        buff.clear()
    buff.append(i)
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            buff.append(j)
            if len(buff) > 4:
                buff.clear()
                break