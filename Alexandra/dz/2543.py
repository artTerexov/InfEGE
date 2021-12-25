with open('24-5.txt') as f:
    a = f.read()
# print(a)
count = 0
for i in range(len(a)-1):
    if a[i] == '(' and a[i + 1] == ')':
        count += 1
    if count == 10000:
        print(i + 1)
        break
