x = 99
d = ''
while x > 0:
    d += str(x % 3)
    x = x // 3
print(d[::-1])

# oyayy