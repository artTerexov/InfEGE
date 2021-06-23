

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = "0" + i * "1" + j * "3" + k * "2"
            while ("01" in s) or ("02" in s) or ("03" in s):
                s = s.replace("01", "2302", 1)
                s = s.replace("02", "10", 1)
                s = s.replace("03", "201", 1)
            if s.count("1") == 60 and s.count("2") == 22 and s.count("3") == 17:
                print(i)
                break