with open('files/3754.txt') as f:
    a = f.read().strip().split('\n')
part = int(a[0].split()[0])
summa = int(a[0].split()[1])
details = [(a[i].split()[0], int(a[i].split()[1]), int(a[i].split()[2])) for i in range(1, len(a))]
details.sort(reverse=True)
budget = 0
for i in range(len(details) - 1):
    if details[i][0] == 'Z':
        budget += details[i][1] * details[i][2]
budget = summa - budget
count = 0
for i in range(-1, -len(details), -1):
    if details[i][0] == 'A':
        if budget >= details[i][1] * details[i][2]:
            budget = budget - details[i][1] * details[i][2]
            count += details[i][2]
        else:
            count_1 = details[i][2]
            while budget >= details[i][1] and count_1 > 0:
                count += 1
                budget -= details[i][1]
                count_1 -= 1
print(count, budget)
