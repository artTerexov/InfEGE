with open('files/4524.txt') as f:
    a = f.read()
count = 0
max_count = 0
t = 0
for i in range(len(a) - 1):
    if a[i] != '.':
        count += 1
    elif count == 0 and a[i] == ".":
        continue
    else:
        t += 1
        if t == 2:
            if count > max_count:
                max_count = count
                count = 0
                t = 0
            else:
                count = 0
                t = 0
        else:
            count += 1
print(max_count)
