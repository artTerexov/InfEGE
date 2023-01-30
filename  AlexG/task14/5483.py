for x in '0123456789abcde':
    num_1 = int('123' + x + '5', 15)
    num_2 = int('1' + x + '233', 15)
    if (num_1 + num_2) % 14 == 0:
        print((num_1 + num_2) / 14)
        break


print(int('1234', 50))