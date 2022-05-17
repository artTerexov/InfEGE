# for i in range(1, 10000):
#     S1 = 0
#     S2 = 0
#     for j in range(len(str(i))):
#         if int(str(i)[j]) % 2 == 0:
#             S1 += int(str(i)[j])
#     for y in range(0,len(str(i)),2):
#         S2 += int(str(i)[y])
# R = abs(S1 - S2)
# if R == 27:
#     print(i)

def s1(n):
    n = str(n)
    summ = 0
    for x in range(len(n)):
        if int(n[x]) % 2 == 0:
            summ += int(n[x])
    return summ


def s2(n):
    summ = 0
    n = str(n)
    for z in range(len(n)):
        if z % 2 == 0:
            summ += int(n[z])
    return summ


for n in range(1, 100000000):
    R = abs(s1(n) - s2(n))
    if R == 27:
        print(n)

