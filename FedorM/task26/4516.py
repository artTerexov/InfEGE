with open('files/26_test') as f:
    s = f.read().strip().split('\n')

cash = 110
money = 0
q = 0
s = [(int(i.split()[0]), i.split()[1]) for i in s]

s.sort()

for i in s:
    if money + i[0] <= cash:
        if i[1] == 'Q':
            q += 1
        money += i[0]
        print(i)

print(q, cash - money)