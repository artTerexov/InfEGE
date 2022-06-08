with open("17.txt") as f:
    s = f.read().split()


nums = [int(i) for i in s]
sred = sum(nums)/len(nums)
s = []
k = 0

for i in range(1, len(nums)-2):
    if (nums[i] * nums[i+1]) > (nums[i-1] * nums[i+2]) and (nums[i] > sred or nums[i + 1] > sred):
        s.append(nums[i] + nums[i+1])


print(max(s), len(s))