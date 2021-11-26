# print("x y z w F")
# for x in (False, True):
#     for y in (False, True):
#         for z in (False, True):
#             for w in (False, True):
#                 f = (x == y) <= (z == w)
#                 if int(f) == 0:
#                     print(int(x), int(y), int(z), int(w), int(f))

print("x y z F")
for x in (False, True):
    for y in (False, True):
        for z in (False, True):
            f = x or y or z
            if int(f) == 1:
                print(int(x), int(y), int(z), int(f))
