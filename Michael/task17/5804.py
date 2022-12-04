def troiki(a: list):
    buff = []
    product = []
    for i in range(len(a) - 2):
        x1 = a[i]
        x2 = a[i + 1]
        x3 = a[i + 2]
        p = 1
        for j in str(x1) + str(x2) + str(x3):
            if int(j) % 2 == 0:
                p *= int(j)
        if p <= 2 * 10 ** 9 and str(p)[:2] == '11' and str(p).count('6', 2) != 0:
            # Считаем произведение всех цифр тройки чисел
            for num in str(x1), str(x2), str(x3):
                result = 1
                for k in num:
                    result *= int(k)
                product.append(result)
            buff.append(result)
    print(len(buff), max(product))
# 113246208
# 455196672000

with open("files/5804") as n:
    x = [int(i) for i in n.readlines()]
    troiki(x)