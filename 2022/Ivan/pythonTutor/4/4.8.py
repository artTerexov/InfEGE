n = int(input())
x = 1
z = 0
for i in range(1, n + 1):
    x *= i
    z += x
print(z)