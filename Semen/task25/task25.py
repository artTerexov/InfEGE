star = [''] + [str(i) for i in range(100)]
count = 0
buff = []
for i in range(1, 10):
    for j in range(10):
        for k1 in star:
            for k2 in star:
                s = int(str(i) + '6' + k1 + '6' + k2 + str(j) + '6')
                if s % 6 == 0 and s % 7 == 0 and s % 8 == 0 and s not in buff:
                    buff.append(s)
buff.sort()
print(buff[:7])

# 56616 162240
# 66696 191040
# 161616 527744
# 166656 523264
# 266616 862680
# 360696 1094400
# 366576 1083264


# 56616 162240
# 66696 191040
# 161616 527744
# 166656 523264
# 266616 862680
# 360696 1094400
# 366576 1083264
