# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [164700; 164752], числа, имеющие ровно 6 различных делителей.
# В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.

buff = []

for i in range(164700, 164752 + 1):
    if len(buff) == 6:
        buff.sort()
        print(buff[4:6:])
        buff.clear()
    else:
        buff.clear()
    buff.append(1),
    buff.append(i)
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            buff.append(j)
        if len(buff) > 6:
            buff.clear()
            break

# 82354 164708
# 54903 164709
# 82358 164716
# 82366 164732