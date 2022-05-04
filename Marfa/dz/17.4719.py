f = open('17-243.txt')
s49 = 0
sob = 0
cnt = 0
s = [int(i) for i in f]
for i in range(len(s)):
    if s[i] % 49 == 0:
        m = s[i]
        while m != 0:
            s49 += m % 10
            m //= 10
for i in range(len(s) - 1):
    if (s[i] < s49 <= s[i + 1] and s[i + 1] % 13 == 0) or (s[i + 1] < s49 <= s[i] and s[i] % 13 == 0):
        cnt += 1
        if s[i] + s[i + 1] > sob:
            sob = s[i] + s[i + 1]
print(cnt, sob)
