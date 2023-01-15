import time

start_time = time.time()

a = 1000000000
c = 0

for i in range(a):
    c += 1

print(c)

print("--- %s seconds ---" % (time.time() - start_time))
