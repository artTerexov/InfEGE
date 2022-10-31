def kingStep(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (abs(x2 - x1) == 1 and y1 == y2) or (abs(y2 - y1) == 1 and x1 == x2):
        return True
    elif abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
        return True
    return False


assert kingStep(5, 5, 4, 4)
assert kingStep(5, 5, 6, 6)
assert kingStep(5, 5, 6, 4)
assert kingStep(5, 5, 4, 6)
assert kingStep(5, 5, 4, 5)
assert kingStep(5, 5, 5, 4)
assert kingStep(5, 5, 6, 5)
assert kingStep(5, 5, 5, 6)

assert kingStep(5, 5, 1, 1)

print('All tests are passed')