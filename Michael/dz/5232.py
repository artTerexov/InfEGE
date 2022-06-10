with open("26-82.txt") as f:
    s = f.read().strip().split('\n')
s.pop(0)

rows = []
for i in s:
    t = i.split()
    rows.append((int(t[0]), int(t[1])))
rows = sorted(rows)

a = []
b = []

max_count = 0
cur = rows[0][0]
max_row = 0
c = 0
for i in range(len(rows)):
    if rows[i][0] == cur and i != len(rows):
        if rows[i][1] % 2 != 0:
            c += 1
    else:
        if c > max_count:
            max_count = c
            max_row = cur
        cur = rows[i][0]
        c = 0
        if rows[i][1] % 2 != 0:
            c += 1

print(max_count, max_row)


