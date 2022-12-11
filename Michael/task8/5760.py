from itertools import product

n = product('АНТИУОПЯ*', repeat=7)
c = 0

for i in n:
    el = ''.join(i)
    if el.count("*") == 1:
        print(el)
        c += 1
print(c)


# a = 'АБВ*ВГД'
# # a = 'Михаил идет гулять'
# print(a.split('*'))