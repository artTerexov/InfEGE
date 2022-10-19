with open('files/2617.txt') as f:
    s = f.read().strip().split()

diskSize = int(s[0])
userNum = int(s[1])
userFiles = [int(s[i]) for i in range(2, len(s))]
buff = []
index = 0
userFiles.sort()

for i in userFiles:
    if sum(buff) + i <= diskSize:
        buff.append(i)
        index += 1
    else:
        break

maximum = 0
for j in range(index + 1, len(userFiles)):
    if sum(buff) - max(buff) + userFiles[j] <= diskSize:
        maximum = max(maximum, userFiles[j])
    else:
        break
print(len(buff), maximum)