with open("24.txt") as f:
    s = f.read().strip()

w = s.split("A")[1:-1]
mx = 0

for i in range(len(w) - 2):
    a = w[i]
    b = w[i + 1]
    c = w[i + 2]
    if a == b == c:
        mx = max(mx, len("A" + a + "A" + b + "A" + c + "A"))
print(mx)

# *,*,*