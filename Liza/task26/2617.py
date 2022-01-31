with open("files/2617.txt") as f:
    s = f.read().strip().split('\n')
diskSize = int(s[0].split()[0])
s.pop(0)
s = [int(i) for i in s]
s.sort()

disk = []

for i in s:
    if sum(disk) + i <= diskSize:
        disk.append(i)
    elif sum(disk) - disk[-1] + i <= diskSize:
        disk[-1] = i

print(len(disk), disk[-1])