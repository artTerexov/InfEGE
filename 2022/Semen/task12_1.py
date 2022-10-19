s = "3" + "9" * 93


while s.find("19") != -1 or s.find("299") != -1 or s.find("3999") != -1:
    s = s.replace("19", "2", 1)
    s = s.replace("299", "3", 1)
    s = s.replace("3999", "1", 1)

print(s)