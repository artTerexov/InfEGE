for a in range(520000, 530000):
    buff = set()
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            buff.add(b)
            buff.add(a // b)
    summ = str(sum(buff))
    if summ == summ[::-1] and len(buff) > 0:
        print(a, max(buff))



# 520211 16781
# 520993 47363
# 521653 47423
# 521947 16837
# 522077 22699