

def f(x, y, z):
    if x == 472 and (z.count('2') + z.count('3')) > z.count('1'):
        return 1
    if x > 472:
        return 0
    return f(x + 3, y, z + '1') + f(x * 2, y, z + '2') + f(x * 7, y, z + '3')


print(f(2, 0, ''))