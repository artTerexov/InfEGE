def f(a, x):
    return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))


for a in range(1, 2000):
    if all([f(a, x) for x in range(1, 2000)]):
        print(a)
        break
# for a in range(1, 2000):
#     nflag = True
#     for x in range(1, 2000):
#         if not(f(a, x)):
#             nflag = False
#             break
#     if nflag:
#         print(a)
#         break
