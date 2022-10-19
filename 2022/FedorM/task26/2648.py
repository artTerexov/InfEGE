with open('files/26-s1.txt') as f:
    s = [int(i) for i in f.read().split()]

s.pop(0)
b = [i for i in s if i <= 100]
b_100 = [i for i in s if i > 100]
b_100.sort()
b_100_sale = b_100[0: len(b_100) // 2]
b_100_not_sale = b_100[len(b_100) // 2:]
print(max(b_100_sale))
b_100_sale = [i * 0.9 for i in b_100_sale]
print(sum(b_100_sale) + sum(b_100_not_sale) + sum(b))