# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...)

A = input().split()

for i in range(0, len(A), 2):
    print(A[i])
