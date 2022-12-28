with open('files/demo') as f:
    s = [[j for j in i.split()] for i in f.readlines()]

time = 0

for process in s:
    if int(process[2]) == 0:
        time += int(process[1])