p = int(input())
x = int(input())
y = int(input())
a = 100 * x + y
b = int(a * (100 + p) / 100)
print(b // 100, b % 100)
