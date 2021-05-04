with open('27-B.txt') as f:
    s = f.read().strip().split('\n')


size = s[0]
s.pop(0)
generator = [int(i) for i in s]
summa = 0
generator.sort()
generator.reverse()

listZero = []
listOne = []
listTwo = []

for i in generator:
    if i % 3 == 0 and len(listZero) < 3:
        listZero.append(i)
    if i % 3 == 1 and len(listOne) < 3:
        listOne.append(i)
    if i % 3 == 2 and len(listTwo) < 3:
        listTwo.append(i)
    if len(listZero) > 3 and len(listTwo) > 3 and len(listOne) > 3:
        break

print(max(sum(listZero), sum(listTwo), sum(listOne), listOne[0] + listZero[0] + listTwo[0]))























# generator.reverse()
#
# for i in range(0, len(generator) - 2):
#     for j in range(1, len(generator) - 1):
#         for n in range(2, len(generator)):
#             first = generator[i]
#             second = generator[j]
#             third = generator[n]
#             summa = first + second + third
#             if summa % 3 == 0:
#                 break
#         if summa % 3 == 0:
#             break
#     if summa % 3 == 0:
#         break
#
# print(summa)
