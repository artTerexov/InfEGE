with open('24-j7.txt') as f:
    s = f.read()

int_s = [int(i) for i in s]
count = 1
maxi = 0
for j in range(1, len(int_s)):
    if int_s[j] % 2 == 0 and int_s[j - 1] % 2 == 0:
        count += 1
    elif int_s[j] % 2 != 0 and int_s[j - 1] % 2 != 0:
        count += 1
    else:
        maxi = max(count, maxi)
        count = 1


print(maxi)
