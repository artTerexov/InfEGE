with open("files/27-b.txt") as f:
    s = f.read().strip().split("\n")
s.pop(0)

summa = 0
diff = []

for i in s:
    num_1 = int(i.split()[0])
    num_2 = int(i.split()[1])
    summa += max(num_2, num_1)
    diff.append(abs(num_1 - num_2))
diff.sort()

if summa % 3 == 0:
    for j in diff:
        if (summa - j) % 3 != 0:
            print(summa - j)
            break
else:
    print(summa)