def optimal(s, n):
    s = s * 2

    prefix = [0] * len(s)
    prefix[0] = s[0]
    for i in range(1, len(prefix)):
        prefix[i] += s[i] + prefix[i - 1]

    s1 = 0
    for i in range(n):
        r = min(i, n - i)
        s1 += s[i] * (r * 2) ** 2

    result = float('inf')
    pointNumber = 0
    for i in range(1, n):
        forward = prefix[i - 1 + n // 2] - prefix[i - 1]
        back = prefix[i - 1 + n] - prefix[i - 1 + n // 2]
        s1 = s1 + back - forward

        if result > s1:
            result = s1
            pointNumber = i + 1
    return pointNumber


def nonOptimal(a):
    m = 9999999
    for i in range(len(a)):
        c = len(a) // 2 * a[i - len(a) // 2]
        for j in range(1, len(a) // 2):
            c += j * a[(i + j) - len(a)] + j * a[i - j]
        if m > c:
            m = c
            h = i + 1
    return h


with open('files/5036_B.txt') as f:
    file = [int(i) for i in f.readlines()]
nn = file.pop(0)

# print(nonOptimal(file))

print(optimal(file, nn))
