# https://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/shoelace/
# 2
# 1
# 3
# 4
# 26

a = int(input())
b = int(input())
l = int(input())
N = int(input())

result = (N - 1) * (b * 2 + a * 2) + a + l * 2

print(result)