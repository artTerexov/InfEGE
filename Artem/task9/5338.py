def condition_one(elements: list) -> bool:
    return elements[-1] < (elements[0] + elements[1] + elements[2])


def condition_two(elements: list) -> bool:
    c = set(elements)
    return len(c) == 3


with open('files/5338') as a:
    d = a.readlines()
count = 0

for i in range(len(d)):
    g = list(map(int, d[i].split('\t')))
    g.sort()
    if condition_one(g) and condition_two(g):
        count += 1
print(count)
