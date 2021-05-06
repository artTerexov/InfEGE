result = 0
for i in range(1, 20):
    result += i * (i + 1)
    print(i, "*", i + 1, "+", end=" ")
print(result)

# A = []
# for i in range(100):
#     if i % 2 == 1:
#         A.append(i)
# print(A)

# count = 0
#
# def f(n):
#     global count
#     count += 1
#     print('*')
#     if n > 0:
#       f(n // 2)
#       f(n // 3)
#
#
# f(8)
# print(count)