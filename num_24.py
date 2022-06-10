
with open("files/24 .txt") as f:
    s = f.read().strip()

w = s.split("A")[1:-1]
mx = 0
for a, b, c in zip(w, w[1:], w[2:]):
    if a == b == c:
        mx = max(mx, len("A" + a + "A" + b + "A" + c + "A"))
print(mx)