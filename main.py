for i in range(10):
    for j in range(10):
        a = int('12345' + str(i) + '6' + str(j) + '8')
        if a % 17 == 0:
            print(a, a // 17)