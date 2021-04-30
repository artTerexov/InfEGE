# def factorial(k):
#     result = 1
#     for i in range(1, k + 1):
#         result *= i
#     return result

def factorial(k):
    if k == 0:
        return 1
    return factorial(k - 1) * k

a = int(input("Введите число для вычесления факториала: "))

print(factorial(a))
