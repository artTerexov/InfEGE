# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [125873; 136762],
# числа, имеющие ровно 5 различных делителей. Выведите количество таких чисел и наибольшее их них.
import time
start_time = time.time()

buff = []
for i in range(125873, 136763):
    d = [1, i]
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            d.append(j)
            if not(i // j in d):
                d.append(i // j)
        if len(d) > 5:
            d.clear()
            break
    if len(d) == 5:
        buff.append(i)

print(len(buff), max(buff))
print("--- %s seconds ---" % (time.time() - start_time))