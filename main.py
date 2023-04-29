a = int(input())
maxnumber = 0
for i in range(a):
    n = int(input())
    if n % 5 == 0 and n > maxnumber:
        maxnumber = n
print(maxnumber)