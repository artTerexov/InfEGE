from itertools import combinations



# Удалили первую строчку из файла

with open('files/2660_test.txt') as f:
    s = [[int(i.split()[0]), int(i.split()[1])] for i in f.readlines()]

sum = 0
raznosti = []
for i in s:
    sum += max(i)
    raznosti.append(max(i) - min(i))

if sum % 3 == 0:
    print(sum - min(raznosti))
else:
    print(sum)
print((sum - 1), (sum - 1) % 3)

# 4 + 7 = 11
# остатки на 3
# 3 + 1 = 4

# 5 + 7 = 12

# 2 + 1 = 3


