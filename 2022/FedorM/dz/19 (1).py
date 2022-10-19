def f(a):
    return (a * 2), (a + 3)


def g(a):
    if a >= 33:
        return 'w'
    if any(g(i) == 'w' for i in f(a)):
        return 'p1'
    if all(g(i) == 'p1' for i in f(a)):
        return 'v1'
    if all(g(i) == 'v1' for i in f(a)):
        return 'p2'
    if all(g(i) == 'p1' or g(i) == 'p2' for i in f(a)):
        return 'v2'


for i in range(1, 33):

    if g(i) == 'v1' or g(i) == 'v2':
        print(i, g(i))
