# ((x ∈ P) → ¬(x ∈ Q)) → ¬(x ∈ А)

# P = [1, 39]

# Q = [23, 58]

P = range(1, 40)
Q = range(23, 59)
A = []

for x in range(-100, 100):
    if (x in P and x in Q) == 1:
        A.append(x)
print(A)
