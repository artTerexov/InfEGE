num = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
base = 6

buff = ""
while num // base > 0:
    buff += str(num % base)
    num = num // base
buff += str(num)

buff = buff[::-1]

print(buff.count("5") - buff.count("0"))

print(9 * 5 ** 4)
