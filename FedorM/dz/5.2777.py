n = 80
x = bin(n)[2:]
x = '0' * (8 - len(x)) + x
x = x.replace('0', 'b')
x = x.replace('1', 'a')
x = x.replace('b', '1')
x = x.replace('a', '0')
x = int(x, 2) + 1
print(x)


