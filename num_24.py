with open("24.txt") as f:
    s = f.read().strip()

w = s.split("A")[1:-1]

buff = []
for i in range(len(w) - 2):
    if w[i] == w[i + 1] == w[i + 2]:
        buff.append(len(w[i]) + len(w[i + 1]) + len(w[i + 2]) + 4)

print(max(buff))