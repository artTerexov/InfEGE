# Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить количество пар элементов (ai, aj)
# этого набора, в которых 1 ≤ i + 7 ≤ j ≤ N и произведение элементов кратно 14.
import time

start_time = time.time()

with open('files/27-13a.txt') as f:
    s_0 = [int(i) for i in f]


with open('files/27-13b.txt') as f:
    s_1 = [int(i) for i in f]


# def func(a):
#     a.pop(0)
#     buff = [i % 14 for i in a]
#     count = 0
#     for i in range(len(a) - 7):
#         m = buff[i + 7:]
#         if buff[i] == 0:
#             count += len(m)
#         elif buff[i] % 2 == 0:
#             count = count + m.count(7) + m.count(0)
#         elif buff[i] == 7:
#             count = count + m.count(2) + m.count(4) + m.count(6) + m.count(8) + m.count(10) + m.count(12) + m.count(0)
#         else:
#             count += m.count(0)
#     return count

# print(func(a))

def func(s):
    L = 7
    s.pop(0)
    queue = [s[i] for i in range(L)]

    count = 0
    D = [[0, 0], [0, 0]]
    for i in range(L, len(s)):
        a = queue.pop(0)
        ind2 = 0 if a % 2 == 0 else 1
        ind7 = 0 if a % 7 == 0 else 1
        D[0][0] += 1
        D[0][1] += (1 - ind7)
        D[1][0] += (1 - ind2)
        D[1][1] += (1 - ind2) * (1 - ind7)
        x = s[i]
        queue.append(x)
        ind2 = 0 if x % 2 == 0 else 1
        ind7 = 0 if x % 7 == 0 else 1
        count += D[ind2][ind7]

    return count


print(func(s_0))
print(func(s_1))
print("--- %s seconds ---" % (time.time() - start_time))
