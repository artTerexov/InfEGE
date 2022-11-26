# count = 0
# for i in range(1, 100000):
#     s = i
#     s //= task15
#     n = 14
#     while s <285:
#         if (s+n) % 9 == 0:
#             s += 11
#         n += 13
#     if n == 118:
#         count += 1
# print(count)
# import itertools
# # s = '0123456789'
# # count = 0
# # a = set(itertools.product(s, repeat=5))
# # for i in a:
# #     n = ''.join(i)
# #     if n[0] != '0' and n[-1] not in '347' and not(n[0]==n[1]==n[2] or n[1]==n[2]==n[3] or n[2]==n[3]==n[4]):
# #         count += 1
# #         # print(n)
# # print(count)
# for i in range(1, 100):
#     s = '5' * (300 + i)
#     while '55555' in s:
#         s = s.replace('55555', '88', 1)
#         s = s.replace('888', '55', 1)
#     print(300+i, s, s.count('5'))

# s = 11 * task15**65+18*task15**38-14*task15**17+19*task15**11+18338
# c = ''
# b = ['A', 'B', 'C', 'D', 'E']
# while s:
#     if s % task15 < 10:
#         c = str(s % task15) + c
#     else:
#         c = b[(s % task15) - task15] + c
#     s //= task15
# print(c)
# print(len(set(c)))

# def F(n):
#     if n <= 1:
#         return 1
#     elif n > 1 and n % 2 == 0:
#         return 3*n+F(n-1)
#     elif n > 1 and n % 2!= 0:
#         return 2*F(n-3)
# print(F(30))
# with open('17.txt') as f:
#     a = [int(i) for i in f]
# cr_znach = sum(a)/len(a)
# b = []
# for i in range(len(a) -1):
#     if a[i] < cr_znach and a[i+1] < cr_znach and (str(a[i])[-1] == '9' or str(a[i+1])[-1]=='9'):
#         b.append(a[i]+a[i+1])
# print(len(b), max(b))
# count = 0
# for i in range(1019, 100000, 1019):
#     for j in range(1019, 100000, 1019):
#         x = i
#         y = j
#         while x != y:
#             if x > y:
#                 x -= y
#             else:
#                 y -= x
#         if x == 1019:
#             count += 1
# print(count)
# def F(a,b, t=''):
#     if a == b and t.count('3')==1:
#         return 1
#     if a > b:
#         return 0
#     return F(a+1,b,t+'1') + F(a+2,b,t+'2') + F(a*2,b,t+'3')
# print(F(2,12))
# count = 0
# for i in range(200000001, 210000000):
#     b = []
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             if j**2 != i:
#                 if j % 2 == 1:
#                     b.append(j)
#                 if (i//j) % 2 == 1:
#                     b.append(i//j)
#             else:
#                 if j % 2 == 1:
#                     b.append(j)
#     if len(b) >= 6 and count<6:
#         count += 1
#         b.sort(reverse=True)
#         print(i, b[5])

with open('files/27A.txt') as f:
    a = [int(i) for i in f]
with open('files/27B.txt') as f:
    b = [int(i) for i in f]


def F(a):
    a.pop(0)
    total_rem = [1] + [0] * 10
    count_amount = 0
    count = 0
    count_unique = 0
    for i in a:
        count_amount += i
        if i % 5 == 0:
            count_unique += 1
        r = count_unique % 11
        count += total_rem[r]
        total_rem[r] += 1
    return count


print(F(a), F(b))

# def F(a,c):
#     if a >= 22 or c>5: return c==3 or c==5
#     if c% 2 ==0:
#         return F(a+1,c+1) or F(a+2,c+1) or F(a*2,c+1)
#     else:
#         return F(a + 1, c + 1) and F(a + 2, c + 1) and F(a * 2, c + 1)
#
# for i in range(1,22):
#     if F(i, 1):
#         print(i)
# with open('24.txt') as f:
#     a = f.readline()
# a = 'ABDSTRE'
# a = a.replace('PR', '.')
# a = a.replace('ST', '*')
# count = 0
# max_count = 0
# t = 0
# for i in range(len(a) - 1):
#     if a[i] != '.' and a[i] != '*':
#         count += 1
#     elif count == 0 and (a[i] == "." or a[i] == "*"):
#         continue
#     else:
#         t += 1
#         if t == 2:
#             if count > max_count:
#                 max_count = count
#                 count = 0
#                 t = 0
#             else:
#                 count = 0
#                 t = 0
#         else:
#             count += 2
# print(max_count)