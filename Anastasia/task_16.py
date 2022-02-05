def F(n):
    # print('*')
    buff.append('*')
    if n >= 1:
        # print('*')
        buff.append('*')
        F(n - 1)
        F(n - 3)
        # print('*')
        buff.append('*')


buff = []
print(F(40))
print(len(buff))
