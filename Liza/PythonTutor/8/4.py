# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
# а используя рекуррентное соотношение a ^ n=a * a ** n-1.

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = float(input())
n = float(input())
print(power(a, n))

