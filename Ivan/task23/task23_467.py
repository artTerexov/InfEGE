
def cal(n, op):
    if n == 32 and op[-2] == '1':
        return 1
    if n > 32:
        return 0
    return cal(n + 1, op + '1') + cal(n * 2, op + '2')


print(cal(5, ''))
