a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        count += 1
print(count)