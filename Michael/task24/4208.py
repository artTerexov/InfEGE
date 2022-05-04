with open("4208.txt") as f:
    s = f.read().split()
count = 0
maxLen = 0
for i in s:
    if i.count('R') < 30:
        for j in range(len(i)):
            end = i.find(i[j], j + 1)
            if end != -1 and (end - j) >= 3:
                # print(i[j], i[j:end + 1])
                count += 1
                length = end - j
                maxLen = max(maxLen, length)


print(maxLen, count)

