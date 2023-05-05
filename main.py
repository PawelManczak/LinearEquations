# Pawel Manczak 188756
import time
from math import sin

from MatrixFunctions import dot_product


def jacobi(A, b, max_iter=1000, epsilon=1e-9):
    time0 = time.time()
    n = len(b)
    x = [0] * n  # początkowe przybliżenie

    for i in range(max_iter):
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
        if error < epsilon * epsilon:
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


def LU_factorization(A, b):
    n = len(A)

    # utworzenie macierzy trójkątnej górnej U i macierzy trójkątnej dolnej L
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # wypełnienie macierzy trójkątnej dolnej L oraz macierzy trójkątnej górnej U
    for j in range(n):
        # wypełnienie j-tej kolumny macierzy U
        for i in range(j, n):
            sum_ = 0.0
            for k in range(j):
                sum_ += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - sum_

        # wypełnienie j-tej kolumny macierzy L
        for i in range(j, n):
            if i == j:
                L[i][j] = 1.0
            else:
                sum_ = 0.0
                for k in range(j):
                    sum_ += L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - sum_) / U[j][j]

    # rozwiązanie układu równań Ax = b na podstawie faktoryzacji LU
    y = [0.0] * n
    x = [0.0] * n
    # rozwiązanie Ly = b (forward substitution)
    for i in range(n):
        sum_ = 0.0
        for j in range(i):
            sum_ += L[i][j] * y[j]
        y[i] = b[i] - sum_
    # rozwiązanie Ux = y (backward substitution)
    for i in range(n - 1, -1, -1):
        sum_ = 0.0
        for j in range(i + 1, n):
            sum_ += U[i][j] * x[j]
        x[i] = (y[i] - sum_) / U[i][i]

    return x


N = 9  # *5*6
A = [[0 for i in range(N)] for j in range(N)]
f = 8
b = [sin(i * (f + 1)) for i in range(N)]

c = dot_product(A, b)
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


print(jacobi(A, b))
print(gauss_seidel(A, b))

print(LU_factorization(A, b))
