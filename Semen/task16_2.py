n = 25468248
count = 0
for i in str(n):
    if int(i) % 2 == 0:
        count += 1
    else:
        break

if count == len(str(n)):
    print("Четное")