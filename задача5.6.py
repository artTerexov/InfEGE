n = input()
s = 0
for i in range(0, len(n), 2):
    if i == 0:
        for j in range(0, int(n[i]) + 1):
            s = s + j
    else:
        s = s - int(n[i])
print(s)