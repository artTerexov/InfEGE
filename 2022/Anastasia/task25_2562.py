a = 17445800000000

count = 0
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        count += 1
        # print(i, a // i)

print(count)


# 2
# 19
# 38
# 4591
# 9182
# 87229
