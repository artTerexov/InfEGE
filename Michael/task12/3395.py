n = "6" * 239
while ("2222" in n) or ("666" in n):
    if "2222" in n:
        n = n.replace("2222", "6", 1)
    else:
        n = n.replace("666", "2", 1)
print(n)