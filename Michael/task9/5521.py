# чтение файла
# /t - табуляция /n - перенос на строку

def countDouble(a: list) -> bool:
    count = 0
    for i in a:
        if a.count(i) == 2:
            count += 1
    return count == 2


def average(a: list) -> bool:
    rep = []
    notRep = []
    for i in a:
        if a.count(i) > 1:
            rep.append(i)
        else:
            notRep.append(i)
    return sum(rep) / len(rep) <= sum(notRep)


with open('5521') as f:
    s = [[int(j) for j in i.split()] for i in f.readlines()]


c = 0
for i in s:
    if countDouble(i) and average(i):
        c += 1

print(c)