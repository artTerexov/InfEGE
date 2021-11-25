import itertools


def check(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] in "0123456789":
            if maximum == "":
                maximum = arr[i]
            elif arr[i] >= maximum:
                maximum = arr[i]
            else:
                return False
    return True


s = "0123456789ABCDEF"
a = set(itertools.product(s, repeat=5))
count = 0
for i in a:
    if i[0] != "0" and check(i):
        print(i)
        count += 1
print(count)
