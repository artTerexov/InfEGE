
def search(buff: list) -> int:
    for i in range(len(buff)):
        if buff[i] in 'AEIOUY':
            return i


def func(a):
    maxx = 0
    n = []
    for i in a:
        if (i != ".") and (((n.count("A") + n.count("E") + n.count("I") + n.count("O") + n.count("U") + n.count("Y")) <= 7) and i not in 'AEIOUY'):
            n.append(i)
            x = (n.count("A") + n.count("E") + n.count("I") + n.count("O") + n.count("U") + n.count("Y"))
            maxx = max(maxx, len(n))
        else:
            if i == '.':
                n = []
            else:
                n = n[search(n) + 1:]
                n.append(i)
                maxx = max(maxx, len(n))

    return maxx


with open("files/4752") as f:
    s = f.readline()


# print('Ответ к задаче:', func(s))
# print('Тест №1', func('BCDGHTHTE.BCDHHCBHEEEEEEEE'))
print('Тест №2', func('BCDGHTHTE.BCDHHCBHEEEEEEEEBCDHHCBHFGFGFG'))
