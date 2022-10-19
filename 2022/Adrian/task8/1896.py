import itertools

s = '0123456789'
a = set(itertools.permutations(s, r=8))
count = 0
for x in a:
    b = ''.join(x)
    if b[0] != '0' and int(b) % 5 == 0:
        check = 0
        for i in range(len(b) - 1):
            if (int(b[i]) % 2 == 0 and int(b[i + 1]) % 2 != 0) or (int(b[i]) % 2 != 0 and int(b[i + 1]) % 2 == 0):
                check += 1
        if check == 7:
            count += 1
print(count)

# 12345678