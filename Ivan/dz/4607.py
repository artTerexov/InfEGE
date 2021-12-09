P = [i for i in range(10, 41)]
Q = [i for i in range(5, 16)]
R = [i for i in range(35, 51)]
X = []
for i in range(-100, 100):
    X.append(i)
    X.append(i + 0.5)
buff = []
for x1 in range(1, 100):
    for x2 in range(x1, 100):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in X:
            if (((10 <= x <= 40) <= (5 <= x <= 15)) or ((not (x1 < x < x2)) <= (35 <= x <= 50))) == 0:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)
print(min(buff))
