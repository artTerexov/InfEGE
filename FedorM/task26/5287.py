d = open('files/26-85.txt').readlines()
d.pop(0)
d = [(int(x.split()[0]), int(x.split()[1]), int(x.split()[2])) for x in d]
d.sort()
for i in range(1, len(d)):
    if d[i - 1][0] == d[i][0]:
        if (d[i][1] - d[i - 1][1]) - 1 == 100 and d[i][2] == d[i - 1][2] == 1:
            s = len([j[2] for j in d if j[2] == 0 and j[0] == d[i][0]])
            if s >= 500:
                print(d[i][0], len([j[2] for j in d if j[2] == 1 and j[0] == d[i][0]]))