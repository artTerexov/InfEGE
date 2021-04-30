from array import *

inputLineOne = input()
lectureNum = int(inputLineOne[0])
pairNum = int(inputLineOne[2])

buff = {}


for i in range(0, pairNum):
    inputLine = input()
    lec1 = int(inputLine[0])
    lec2 = int(inputLine[2])
    if lec2 in buff:
        buff[lec2]
    else:
        buff.setdefault(lec2, [lec1])
print(buff)