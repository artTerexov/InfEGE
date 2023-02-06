#*1?*?68*
#j - ?
#i - *
count = 0
for j in range(10):
    for k in range(10):
        num = int('1' + str(j) + str(k) + '68')
        if num <= 17000000 and num % 161 == 0:
            count+=1
            print(num, num//161, count)
for j in range(10):
    for k in range(10):
        for i in range(10):
            for a in range(10):
                for b in range(10):
                    num = int(str(i) + str(a) + str(b) + '1' + str(j) + str(k) + '68')
                    if num <= 17000000 and num % 161 == 0:
                        count += 1
                        print(num, num // 161, count)


for j in range(10):
    for k in range(10):
        for i in range(10):
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        for d in range(10):
                            for e in range(10):
                                num = int(str(i) + str(a) + str(b) + '1' + str(j) + str(c) + str(d) + str(e) + str(k) + '68')
                                if num <= 17000000 and num % 161 == 0:
                                    count += 1
                                    print(num, num // 161, count)
for j in range(10):
    for k in range(10):
        for i in range(10):
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        for d in range(10):
                            for e in range(10):
                                for f in range(10):
                                    for g in range(10):
                                        for h in range(10):
                                            num = int(str(i) + str(a) + str(b) + '1' + str(j) + str(c) + str(d) + str(e) + str(k) + '68' + str(f) + str(g) + str(h))
                                            if num <= 17000000 and num % 161 == 0:
                                                count += 1
                                                print(num, num // 161, count)