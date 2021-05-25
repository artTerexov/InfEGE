with open('27-B.txt', 'r') as F:
    s = F.read().strip().split("\n")

s.pop(0)
summa = 0
diff = []

for i in s:
    numOne = int(i.split()[0])
    numTwo = int(i.split()[1])
    summa += max(numOne, numTwo)
    diff.append(abs(numOne - numTwo))

diff.sort()

if summa % 3 == 0:
    for j in diff:
        if (summa - j) % 3 != 0:
            print(summa - j)
            break
else:
    print(summa)
