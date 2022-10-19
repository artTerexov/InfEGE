with open("files/17-4322.txt") as f:
    s = [int(i) for i in f.read().split()]

a = []
# for i in s:
#     if i[3] == "5" or i[3] == "7":
#         a.append(i)
#
# b = []
# for i in a:
#     if int(i) % 9 != 0 and int(i) % 11 != 0:
#         b.append(i)

for i in s:
    if (i % 10 == 5 or i % 10 == 7) and i % 9 != 0 and i % 11 != 0:
        a.append(i)


d = max(a)
c = min(a)
print(len(a), int(d) + int(c))