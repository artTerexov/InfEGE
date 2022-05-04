s = open('files/17-4.txt')
a = [int(x) for x in s.readlines()]

#
# buff = []
#
# for i in a:
#     if int(str(i)[-2]) <= 4 and 3 <= int(str(i)[-3]) <= 7:
#         buff.append(i)
#
# print(len(buff), min(buff))