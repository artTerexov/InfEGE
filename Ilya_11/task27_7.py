with open("27-A (1).txt") as f:
    s = f.read().strip().split("\n")
s.pop(0)

listOne = []
listTwo = []
listThree = []

diff_1_3 = []
diff_2_3 = []
for i in s:
    a, b, c = sorted(map(int, i.split()))
    listOne.append(a)
    listTwo.append(b)
    listThree.append(c)
    diff_1_3.append(c - a)
    diff_2_3.append(c - b)

# print(listOne)
# print(listTwo)

sumThree = sum(listThree)
d = diff_2_3
d.sort()
print(d)
badIndex = -1
print(d)
print(sum(listTwo))
if sum(listTwo) % 2 != 0:
    for j in d:
        badIndex = diff_2_3.index(j)
        if (sum(listTwo) + j) % 2 == 0:
            # print(sum(listTwo) - listTwo[indx] + listThree[indx])
            sumThree -= j
            print(j)
            print(diff_1_3[badIndex])
            break

d = diff_1_3
d.sort()
print(d)
print(sum(listOne))
if sum(listOne) % 2 != 0:
    for t in d:
        if diff_1_3.index(t) == badIndex:
            continue
        if (sum(listOne) + t) % 2 == 0:
            # print(sum(listTwo) - listTwo[indx] + listThree[indx])
            sumThree -= t
            print(t)
            print(diff_2_3[diff_1_3.index(t)])
            break

print(sumThree)


