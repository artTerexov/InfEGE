# – в строке есть хотя бы одно повторяющееся число;
# – сумма неповторяющихся чисел строки нечётная.

a = open('files/9-176')
d = a.readlines()
a.close()


# в строке есть хотя бы одно повторяющееся число;
def cond_1(g: list):
    g = set(g)
    return len(g) <= 6


# сумма неповторяющихся чисел строки нечётная.
def cond_2(g:list):

    return


c = 0
for i in range(len(d)):
    g = list(map(int, d[i].split('\t')))
    if test1(g):
        c += 1
        # print(g)
print(c)