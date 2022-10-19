# 5 задание с сайта ниже
# https://4ege.ru/informatika/65775-demoversija-ege-2023-po-informatike.html

for n in range(1, 100):
    N = bin(n)[2:]
    if N.count('1') % 2 == 0:
        N = '10' + N[2:] + '0'
    elif N.count('1') % 2 != 0:
        N = '11' + N[2:] + '1'
    R = int(N, 2)
    if R > 40:
        print(n)