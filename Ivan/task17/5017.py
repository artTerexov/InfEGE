def in5(a):
    n = ''
    while a > 0:
        n += str(a % 5)
        a = a // 5
    return n[::-1]


with open("files/5017.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]
ssum = 0
buff = []
z5 = 0
for i in range(len(s)):
    if s[i] % 32 == 0:
        z5 = in5(s[i]).count("3")
        ssum += z5 * 3
for i in range(len(s) - 2):
    if s[i] > ssum or s[i + 1] > ssum or s[i + 2] > ssum:
        buff.append(s[i] + s[i + 1] + s[i + 2])
print(len(buff), max(buff))
