c = 0
def f(n):
    if n > 25: return (2*n*n*n + 1)
    if n <= 25: return(f(n+2) + 2*f(n + 3))
for n in range(1,1000):
    if f(n) % 11 == 0:
        c += 1
print(c)