with open("24.txt") as f:
    s = f.read().split('A')

a = []

for i in range(len(s) - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        a.append(len(s[i]) + len(s[i + 1]) + len(s[i + 2]) + 4)
print(max(a))


# 0 1 2 3 4 5 6 7 8 9
# A D B A D B A D B A