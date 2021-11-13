# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4220

for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "10" + b + "11"
    else:
        b = "1" + b + "00"
    r = int(b, 2)
    if r > 1023:
        print(r)
        break