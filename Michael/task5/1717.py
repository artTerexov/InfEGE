count = 0
for i in range(700, 801):
    nums = [k for k in str(i)]
    nums.sort()
    maxNum = int(nums[-1] + nums[-2])
    if i % 100 == 0:
        minNum = maxNum
    elif nums[0] == '0':
        minNum = int(nums[-2] + nums[-1])
    else:
        minNum = int(nums[0] + nums[1])
    if maxNum - minNum == 80:
        count += 1
        print(i, maxNum, minNum)
print(count)
# [1, 2, 3]