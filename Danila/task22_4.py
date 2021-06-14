# Укажите наибольшее трёхзначное натуральное число, при
# вводе которого эта программа напечатает сначала 2, потом – 7

# for i in range(1, 1000):
#     x = i
#     a=0
#     b=1
#     while x > 0:
#         if x%2 > 0:
#             a += x%6
#         else:
#             b += x%6
#         x = x//6
#     if a == 2 and b == 7:
#         print(i)

for i in range(1, 1000):
    x = i
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += x % 6
        else:
            b += x % 6
        x = x // 6
    # print(a, b)
    if a == 2 and b == 7:
        print(i)
