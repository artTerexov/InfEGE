def convert(x, n):
    digits = ""
    while x:
        digits += str(x % n)
        x //= n
    return digits[:: -1]


t = convert(3 ** 3 * 7 ** 69 - 70, 7)
count = 0
for i in range(0, len(t)):
    if t[i] == "4":
        count += 1
print(count)
