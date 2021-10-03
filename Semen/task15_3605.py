# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3605

def dell(n, m):
    return n % m == 0


A = 1024
while True:
    found = False
    for x in range(1, 1000):
        if not ((dell(x, 84) and dell(x, 90)) or (not dell(x, A))):
            found = True
            break
    if not found:
        print(A)
        break
    A += 1
