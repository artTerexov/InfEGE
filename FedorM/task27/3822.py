import itertools

with open('files/3822_test.txt') as f:
    s = f.read().strip().split('\n')

s = [int(i) for i in s][1:]
count = 0
countA = [0, 0, 0]
for i in range(1, len(s) + 1):
    comb = itertools.combinations(s, r=i)
    for i in comb:
        if sum(i) % 3 == 0:
            count += 1
        countA[sum(i) % 3] += 1
print(count, countA)

# f = open('files/3822_B.txt')
# n = int(f.readline())
#
# k = [0, 0, 0]
#
# for i in range(n):
#     x = int(f.readline())
#     k1 = k.copy()
#     for i in range(3):
#         k1[(i+x)%3]+=k[i]
#     k1[x%3]+=1
#     k = k1.copy()
# print(k[0])
#
# # O(n)
#
# f.close()