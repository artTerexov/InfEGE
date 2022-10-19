s = "1" * 30 + "23" * 30

while ("21" in s) or ("23" in s):
    if "21" in s:
        s = s.replace("21", "11", 1)
    else:
        s = s.replace("23", "21", 1)

print(s.count("1"))