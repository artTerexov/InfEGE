import string
d = open('files/3783.txt').read().strip().split('\n')
h = []
A = string.ascii_uppercase

for i in range(len(d)):
    c = 0
    for j in range(1, len(d[i])):
        if ord(d[i][j - 1]) - ord(d[i][j]) == -1:
            c += 1
    h.append((c, i))

minIndex = min(h)[1]
print(min(h))
letterNum = [(d[minIndex].count(i), i)for i in A]

print(max(letterNum))

print(''.join(d).count('W'))


