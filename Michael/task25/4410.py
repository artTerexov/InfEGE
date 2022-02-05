count = 0
nums = []
max_dls = []

for num in range(520000, 100000000):
    if count >= 5:
        break
    dls = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            dls.add(i)
            dls.add(num // i)
    t = str(sum(dls))
    if t == t[::-1] and len(dls) > 1:
        nums.append(num)
        max_dls.append(max(dls))
        count += 1

# 520211 16781
# 520993 47363
# 521653 47423
# 521947 16837
# 522077 22699


for i in range(0, len(nums)):
    print(nums[i], max_dls[i])