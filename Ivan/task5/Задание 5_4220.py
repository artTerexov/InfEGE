for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 != 0:
        a = "10" + b + "11"
    else:
        a = "1" + b + "00"
    R = int(a, 2)
    if R > 1023:
        print(R)
        break
