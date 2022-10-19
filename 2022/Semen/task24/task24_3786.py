with open("files/3786.txt") as f:
    buff = f.read()

s = buff.strip().split()
maxStr = 0
maxCount = 0

for i in range(len(s)):
    count = 0
    for j in range(len(s[i]) - 1):
        if s[i][j] == s[i][j + 1]:
            count += 1
        else:
            if maxCount < count:
                maxCount = count
                maxStr = i
            count = 1

elementSet = set(s[maxStr])
maxElem = ""
maxCountElem = 0

for letter in elementSet:
    if maxCountElem < s[maxStr].count(letter):
        maxCountElem = s[maxStr].count(letter)
        maxElem = letter

print(maxElem, buff.count(maxElem))