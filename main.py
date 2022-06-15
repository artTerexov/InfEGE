# for i in range(1, 10):
#     if i == 4:
#         print('OK', i)

W = '1010011'
# print(W.count('1'), W.count('0'), W.count('1') == W.count('0'))

if W.count('1') == W.count('0'):
    W = W + W[-1]