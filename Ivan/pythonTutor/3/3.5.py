a = int(input())
a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
h = a // 60 + 9
m = a % 60
print(h, m)
