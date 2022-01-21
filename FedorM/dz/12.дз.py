x = '8' * 62
while x.count('222') or x.count('888'):
    if x.count('222'):
        x = x.replace('222', '8', 1)
    else:
        x = x.replace('888', '2', 1)
print(x)