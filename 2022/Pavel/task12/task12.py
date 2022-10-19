for i in range(1, 30):
    for j in range(1, 30):
        for k in range(1, 30):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 111 and s.count('2') == 101 and s.count('3') == 35:
                print(i + j + k + 2)