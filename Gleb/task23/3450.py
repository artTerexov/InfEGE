def f(num, call):
    if num > call:
        return 0
    if num == call:
        return 1
    return f(num + 1, call) + f(num + 5, call) + f(num * 3, call)


n = 1
result = 0
while result != 175:
    n += 1
    result = f(1, n)

print(n)