for i in range(1820348, 2880927 + 1):
    b = []
    count = 0
    if int(i ** 0.5) ** 2 != i:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            if j ** 2 == i:
                b.append(j)
            else:
                b.append(j)
                b.append(i//j)
                count += 1
        if count > 1:
            break
    if len(b) == 3:
        print(max(b), i)
