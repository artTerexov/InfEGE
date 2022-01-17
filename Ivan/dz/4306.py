def arifma(n1, n2, n3):
    sum = (n1 + n2 + n3) // 3
    return sum


with open("4306.txt") as f:
    s = f.read().strip().split("\n")

buff = []
cnt = 0
s = [int(i) for i in s]
for i in range(len(s) - 2):
    if (s[i] % 3 == 0 and s[i + 1] % 3 == 0 and s[i + 2] % 3 == 0) and (s[i] % 12 == 0 or s[i + 1] % 12 == 0 or s[i + 2] % 12 == 0):
        buff.append(arifma(s[i], s[i + 1], s[i + 2]))
        cnt += 1
print(cnt, min(buff))

# def check():
#     print("Its function")
#     return True
#
#
# a = True
#
# # 1 or 0
#
# if a or check():
#     print("OK")
