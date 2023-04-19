a = int(input())

hasZero = "NO"
maxResult = 0

for i in range(a):
    num = int(input())
    if num == 0:
        hasZero = "YES"
    if num > maxResult:
        maxResult = num
print(maxResult)
print(hasZero)

