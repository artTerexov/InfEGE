# with open('24-5.txt') as f:
#     s = f.read()
#
# # s = '()(())()'
# # o = s.count('(')
# # index = 1
# # while s.count('(') >= o - 10000:
# #     s = s[1:]
# #     index += 1
# #     if s.count('(') < o - 10000:
# #         index += s.find('(')
#
# # print(index)
#
# count = 0
# for i in range(len(s) - 1):
#     if s[i] == "(" and count == 9999:
#         index = i + 1
#     if s[i] == "(" and s[i + 1] == ")":
#         count += 1
#
# print(index)

# def deliteli(n):
#     array = []
#     if n ** 0.5 % 1 != 0:
#         return 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             array.append(i)
#             if not(n // i in array):
#                 array.append(n // i)
#         if len(array) > 5:
#             break
#     if len(set(array)) == 5:
#         array.sort()
#         print(array[-2], array[-1])
#         return 1
#
#
# for j in range(1820348, 2880927 + 1):
#     if deliteli(j):
#         continue

# with open('27-18b.txt') as f:
#     s = f.read().strip().split('\n')
#
#
# size = s[0]
# s.pop(0)
# generator = [int(i) for i in s]
# count = 0
# for j in range(0, len(generator) - 1):
#     for h in range(j + 1, j + 5):
#         if h > len(generator) - 1:
#             break
#         proiz = generator[j] * generator[h]
#         summa = generator[j] + generator[h]
#         if proiz % 13 == 0 and summa % 2 != 0:
#             count += 1
# #
# # print(count)
#
#
# import string
# import time
#
# def is_pangram(s):
#     template = {i for i in range(65, 91)}
#     buff = set()
#     s = s.upper()
#     for i in s:
#         if 65 <= ord(i) <= 90:
#             buff.add(ord(i))
#     if template == buff:
#         return 1
#     else:
#         return 0
#
# # def is_pangram(s):
# #     return set(string.ascii_lowercase) <= set(s.lower())
#
# start_time = time.time()
#
# pangram = "The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog! The quick, brown fox jumps over the lazy dog!"
#
# print(is_pangram(pangram))
# print("--- %s seconds ---" % (time.time() - start_time))
# all

print(2 ** 4)
