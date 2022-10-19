# Автор: 99 баллов

file = open("files/26-84.txt")
n = int(file.readline())
a = sorted(list(map(int, file.readline().split())))
b = sorted(list(map(int, file.readline().split())))
cnt = [0] * n
j = 0
for i in range(n):
    while j < n and a[j] <= b[i]:
        j += 1
    cnt[i] = j
res = 1
maxRes = 1
for i in range(n):
    res *= (cnt[i] - i)
    # res %= 100000007
    maxRes *= (i + 1)
    # maxRes %= 100000007
print(res, cnt[0])
