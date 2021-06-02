b = []
for i in range(1012, 9639):
    if i % 10 == 6 and i % 4 != 0 and i % 5 != 0:
        b.append(i)
print(len(b), max(b), min(b))