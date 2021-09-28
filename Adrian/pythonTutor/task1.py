h = int(input())
a = int(input())
b = int(input())

h_remain = h - a
h_day = a - b

if h_remain % h_day == 0:
    z = h_remain // h_day + 1
else:
    z = h // h_day

print(z)