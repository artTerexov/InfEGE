# with open('files/4042_test.txt') as f:
with open('files/4042.txt') as f:
    s = f.readlines()

maxRange = 0
for i in s:
    if i.count('E') < 20:
        for j in range(len(i)):
            startIndex = j
            endIndex = i.rfind(i[j])
            maxRange = max(maxRange, endIndex - startIndex)
print(maxRange)
# afdsafsga