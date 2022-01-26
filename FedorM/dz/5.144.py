z = ''
for i in range(10000, 100000):
    i = str(i)
    x = int(i[0]) + int(i[2]) + int(i[4])
    y = int(i[1]) + int(i[3])
    if x > y:
        z = str(y) + str(x)
    if x <= y:
        z = str(x) + str(y)
    if int(z) == 621:
        print(i)
        break
