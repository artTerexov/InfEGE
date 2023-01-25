with open('files/4518.txt') as f:
    s = [[int(i.split()[0]), i.split()[1]] for i in f.readlines()]

money = int(s[0][1])

s.pop(0)
s.sort()

total = 0
sold = []
for i in s:
    if total + i[0] <= money:
        sold.append(i)
        total += i[0]
    elif i[1] == 'A':
        for j in range(len(sold) - 1, -1, -1):
            if sold[j][1] != 'A' and total - sold[j][0] + i[0] <= money:
                total = total - sold[j][0] + i[0]
                sold[j] = i
                break
count = 0
for k in sold:
    money -= k[0]
    if k[1] == 'A':
       count += 1
print()