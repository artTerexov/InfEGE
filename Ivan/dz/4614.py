P = [i for i in range(5, 110)]
Q = [i for i in range(15, 42)]
R = [i for i in range(25, 70)]
buff = []
for x1 in range(1, 100):
    for x2 in range(x1, 100):
        A = [i for i in range(x1, x2 + 1)]
        flag = True
        for x in range(-100, 100):
            if (((x in P) <= (x in Q)) or ((not (x in A)) <= (not(x in R)))) == 0:
                flag = False
                break
        if flag:
            buff.append(x2 - x1)
print(min(buff))