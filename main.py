import random

task3 = [i for i in range(1, 18)]
task3.pop(task3.index(5))
task3.pop(task3.index(17))
task3.pop(task3.index(14))
task3.pop(task3.index(2))
task3.pop(task3.index(15))
task3.pop(task3.index(12))
task3.pop(task3.index(8))
task3.pop(task3.index(7))
task3.pop(task3.index(11))
task3.pop(task3.index(13))
task3.pop(task3.index(10))
task3.pop(task3.index(6))
task4 = []
task5 = [1, 2, 6, 14, 16, 17]

r3 = random.randint(0, len(task3) - 1)
r5 = random.randint(0, len(task5) - 1)

print(task3[r3], task5[r5])