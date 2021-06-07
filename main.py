import random

task3 = [i for i in range(1, 18)]
task3.pop(task3.index(5))
task3.pop(task3.index(17))
task3.pop(task3.index(14))
task3.pop(task3.index(2))
task3.pop(task3.index(15))
task3.pop(task3.index(12))
task4 = [1, 2, 18]
task5 = [1, 2, 3, 6, 7, 8, 11, 12, 13, 14, 16, 17]

r3 = random.randint(0, len(task3) - 1)
r4 = random.randint(0, len(task4) - 1)
r5 = random.randint(0, len(task5) - 1)

print(task3[r3], task4[r4], task5[r5])