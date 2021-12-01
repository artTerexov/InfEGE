import time


def binarySearch(value, a):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return False
    else:
        return True


start_time = time.time()
with open('files/3762.txt') as f:
    a = f.read().strip().split('\n')

b = [int(a[i]) for i in range(1, len(a))]
b.sort()
troika = []
for i in range(len(b) - 2):
    for j in range(i + 1, len(b) - 1):
        for h in range(j + 1, len(b)):
            s = b[i] + b[j] + b[h]
            sr = s // 3
            if s % 3 == 0 and binarySearch(sr, b):
                troika.append(sr)
print(len(troika), min(troika))

print("--- %s seconds ---" % (time.time() - start_time))