with open("files/2617.txt") as f:
    s = f.read().split()

diskSize = int(s[0])
userNumber = int(s[1])
userFiles = [int(s[i]) for i in range(2, len(s))]

userFiles.sort()
lastIndex = 0
buff = []

for i in range(userNumber):
    if sum(buff) + userFiles[i] <= diskSize:
        buff.append(userFiles[i])
        lastIndex = i
    else:
        break

buff.pop(-1)

for j in range(lastIndex, userNumber):
    if sum(buff) + userFiles[j] <= diskSize:
        continue
    else:
        buff.append(userFiles[j - 1])
        break

print(len(buff), max(buff))