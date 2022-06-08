with open("files/5060.txt") as f:
    s = f.read().strip().split("\n")


s = [int(i) for i in s]
buff = []
maxx = 7
for i in range(len(s) - 1):
    while s[i] != 0:
        result = ''
        result += str(s[i] % 3)
        s[i] = s[i] // 3
    result = result[::-1]
    for j in range(len(result)):
        summ = 0
        summ += int(result[j])
        if summ == maxx:
            buff.append(s[i] + s[i + 1])
print(len(buff), min(buff))




# for i in range(len(s)):
#     if s[i] % 11 == 0:
#         maxx.append(s[i])
# print(max(maxx))