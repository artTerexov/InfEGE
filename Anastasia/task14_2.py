num = 4 * 343 ** 5 + 6 * 49 ** 8 - 50
base = 7
buff = ''
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)
buff = buff[::-1]
print(buff.count('6'))

