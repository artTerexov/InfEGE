# 7∙512**3200 + 6∙256**3100 – 5∙64**3000 – 4∙8**2900 – 1542

num = 7 * 512**3200 + 6*256**3100 - 5*64**3000 - 4*8**2900 - 1542

base = 64
count = 0

while num != 0:
    if num % base == 0:
        count += 1
    num = num // base

print(count)
