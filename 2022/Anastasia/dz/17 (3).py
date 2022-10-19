with open('17 пробник.txt') as f:
    s = f.read().strip().split('\n')
s = [int(i) for i in s]
buff = []
maxEl = 0
for j in s:
    if j % 11 == 0:
        maxEl = max(maxEl, j)
for i in range(0, len(s) - 1):
    num_1 = s[i]
    num_2 = s[i + 1]
    if (num_1 % 11 == 0 or num_2 % 11 == 0) and (num_1 + num_2) <= maxEl:
        buff.append(num_1 + num_2)
print(len(buff), max(buff)) 