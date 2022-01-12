
f = open("files/27-26a.txt")
a = f.read().strip()
f.close()

generator = [i for i in a.split("\n")]

pairNum = int(generator[0])
generator.pop(0)

D = 16
summa = 0
dMin = [100000] * D

for pair in generator:
    numOne = int(pair.split()[0])
    numTwo = int(pair.split()[1])
    summa += min(numOne, numTwo)
    d = abs(numTwo - numOne)
    r = d % D
    if r > 0:
        dMinNew = dMin.copy()
        for k in range(1, D):
            r0 = (r + k) % D
            dMinNew[r0] = min(d + dMin[k], dMinNew[r0])
        dMinNew[r] = min(dMinNew[r], d)
        dMin = dMinNew

if summa % 16 == 15:
    print(summa)
else:
    print(summa + dMin[15 - (summa % 16)])

