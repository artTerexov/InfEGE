def double(a: list):
    l = len(a)
    minn = 100000
    buff = []
    for i in a:
        if i > 0 and i % 19 == 0:
            minn = min(minn, i)
    for i in range(l - 1):
        if a[i] + a[i + 1] < minn:
            buff.append(a[i] + a[i + 1])
    print(len(buff), max(buff))


with open("files/5373") as x:
    n = [int(i) for i in x.readlines()]
    double(n)