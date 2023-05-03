# Pawel Manczak 188756
import time
from math import sin

from MatrixFunctions import dot_product


def solve_jacobi(A, b, max_iterations=1000, tolerance=1e-9):
    time0 = time.time()
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
            print("Jacobi's method")
            print('time:', time.time() - time0)
            print('iterations:', i)
            return x_new

        x = x_new

    raise Exception("Metoda Jacobiego nie zbiega się")


def gauss_seidel(A, b, max_iter=1000, epsilon=1e-6):
    time0 = time.time()

    n = len(A)
    x = [0] * n

    for k in range(max_iter):
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]
            x[i] = (b[i] - s) / A[i][i]

        r = [b[j] - dot_product(A[j], x) for j in range(n)]
        error = dot_product(r, r)
        if error < epsilon * epsilon:
            print("Gaus_seidel method")
            print('time:', time.time() - time0)
            print('iterations:', i)
            return x

    raise Exception("Metoda Gausa-Seidla nie zbiega się")


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
print(gauss_seidel(A, b))
