# Pawel Manczak 188756
from math import sin

from MatrixFunctions import dot_product


def solve_jacobi(A, b, max_iterations=1000, tolerance=1e-9):
    n = len(b)
    x = [0] * n  # początkowe przybliżenie

    for i in range(max_iterations):
        x_new = [0] * n

        # obliczanie nowych wartości x_i
        for j in range(n):
            s = 0
            for k in range(n):
                if k != j:
                    s += A[j][k] * x[k]
            x_new[j] = (b[j] - s) / A[j][j]

        # sprawdzanie warunku zakończenia
        r = [b[j] - dot_product(A[j], x_new) for j in range(n)]
        error = dot_product(r, r)
        if error < tolerance * tolerance:
            return x_new

        x = x_new

    raise Exception("Metoda Jacobiego nie zbiega się")




N = 9  # *5*6
A = [[0 for i in range(N)] for j in range(N)]

e = 7
a1 = 5 + e
for i in range(N):
    A[i][i] = a1

a2 = -1
for i in range(N - 1):
    j = i + 1
    A[i][j] = a2
    j = i - 1
    A[i][j] = a2

a3 = -1
for i in range(N - 2):
    j = i + 2
    A[i][j] = a3
    j = i - 2
    A[i][j] = a3

# print(A)

f = 8
b = [sin(i * (f + 1)) for i in range(N)]

c = dot_product(A, b)

v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(dot_product(v1, v2))

print(solve_jacobi(A, b))

