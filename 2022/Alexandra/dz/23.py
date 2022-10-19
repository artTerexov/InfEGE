def calc(num):
    if num == 8:
        return 1
    if num < 10:
        return 0
    m = str(num)
    return calc(int(m[0]) + int(m[1])) + calc(int(m[0]) * int(m[1]))


count = 0
for i in range(10, 100):
    if calc(i):
        count += 1
print(count)