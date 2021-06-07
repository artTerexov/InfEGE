n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        c = 0
        while n % i == 0:
            c = c + 1
            n = n // i
        if c > 1 and n != 1:
            print(i, "^", c, "*", end="", sep="")
        elif c == 1 and n != 1:
            print(i, "*", end="", sep="")
        elif c == 1 and n == 1:
            print(i, end="", sep="")
        elif c > 1 and n == 1:
            print(i, "^", c, end="", sep="")



