with open('files/2559.txt') as f:
    s = f.read().strip().split('\n')

countString = 0
for i in s:
    for j in range(len(i) - 3):
        if i[j] == 'Z' and i[j + 2] == 'R' and i[j + 3] == 'O':
            countString += 1
            break
print(countString)