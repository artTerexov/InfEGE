# https://4ege.ru/informatika/60050-demoversija-po-informatike-ege-2021.html

def stones(s1, s2, n, way):
    way += str(s1) + " " + str(s2) + "\n"
    if n < 2 and s1 + s2 >= 77:
        return 0
    elif n == 3 and s1 + s2 < 77:
        return 0
    elif s1 + s2 >= 77 and n == 3:
        print(way)
        return 1
    return stones(s1 + 1, s2, n + 1, way) + stones(s1 * 2, s2, n + 1, way) + stones(s1, s2 + 1, n + 1, way) + stones(s1, s2 * 2,
                                                                                                            n + 1, way)


# for S in range(1, 70):
#     # print(S, stones(18, 7, 0, ""))
#     stones(31, 7, 0, "")
stones(31, 7, 0, "")
