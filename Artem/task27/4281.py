with open('files/27-75b.txt') as f:
    a = f.read().strip().split('\n')
a.pop(0)
a = list(map(int, a))
D = 43
c = 0
maxSum = 0
maxLen = 0
for i in range(len(a)):
    x = i
    k = 0
    while x != (len(a)):
        k = a[x] + k
        x += 1
        if k % D == 0 and maxSum <= k:
            if maxSum == k:
                maxLen = min(maxLen, x - i)
            else:
                maxLen = x - i
            maxSum = k
print(maxLen)