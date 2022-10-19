def f(a):
    c = str(a)
    count = 0
    for i in c:
        count += int(i)
    return count


with open('files/3738(kompege).txt') as fi:
    a = [int(i) for i in fi]
b = []

for i in range(1, len(a) - 1):
    if f(a[i - 1]) == f(a[i + 1]):
        b.append(f(a[i]))
print(len(b))


def most_frequent(List):
    return max(set(List), key=List.count)


print(most_frequent(b))
