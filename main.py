for i in range(1, 1000):
    a = ("1" * i) + ("3" * 15)
    # print(a)
    while "13" in a:
        a = a.replace("13", "5", 1)
    count = 0
    for j in a:
        count += int(j)
    if count == 63:
        print(i)
