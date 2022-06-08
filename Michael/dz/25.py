def get_sum(num):
    num = str(num)
    s = 0
    for i in num:
        s += int(i)
    return s


def check1(num):
    num = str(num)
    for i in range(0, len(num)-3):
        if num[i] == "0" and num[i+3] == '3':
            return True
    return False


def check2(num):
    num = str(num)
    if num[:-1] == "2" and num[:-4] == "4":
        return True
    else:
        return False


def check3(num):
    num = str(num)
    if "1" in num:
        return True
    else:
        return False


def check(num):
    if num % 13 == 0 and not check1(num) and not check2(num) and not check3(num):
        return True
    else:
        return False


num = 700000
a = []
while len(a) < 5:
    if check(num):
        a.append(num)
    num += 1

for i in a:
    print(i, get_sum(i))