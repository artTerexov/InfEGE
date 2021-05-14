for i in range(2, 100):
    a = str(bin(i))[2::]
    for j in range(0, 3):
        if a.count("0") == a.count("1"):
            a += a[-1]
        elif a.count("0") > a.count("1"):
            a += "1"
        elif a.count("0") < a.count("1"):
            a += "0"
    if int(a, 2) % 4 == 0 and int(a, 2) % 8 != 0:
        print(i)



