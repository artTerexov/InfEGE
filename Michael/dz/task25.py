def get_num_and_del(num):
    d = 18
    while d <= (num/8)+1:
        if num % d == 0:
            return d
        d += 10

    return False


answer_dels = []
answer_nums = []

num = 500000
count = 0
while True:
    if count >= 5:
        break
    t = get_num_and_del(num)
    if t:
        answer_dels.append(t)
        answer_nums.append(num)
        count += 1
    num += 1


print(answer_nums, answer_dels)
