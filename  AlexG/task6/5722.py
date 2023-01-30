count = 0
for N in range(1000, 9999):
    n = str(N)
    if int(n[0]) % 4 == 0:
        n = "9" + n[1:]
    if int(n[0]) % 2 == 0 and int(n[0]) % 4 != 0:
        n = "3" + n[1:]
    R = int(n)
    if str(R)[0] == "9" and oct(R)[-1] == '4':
        count += 1

print(count)


