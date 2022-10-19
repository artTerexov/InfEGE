def summa(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result % 5 == 0


with open("files/4316.txt") as f:
    s = f.read().strip().split("\n")
s = [int(i) for i in s]
buff = []


for i in range(len(s)):
    if summa(s[i]) and (s[i] % 3 != 0 or s[i] // 3 % 3 != 0):
        buff.append(s[i])

print(len(buff), max(buff))