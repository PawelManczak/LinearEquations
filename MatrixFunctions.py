def dot_product(A, B):
    if isinstance(A[0], list) and isinstance(B, list):
        # A i B są macierzami
        lenB0 = 0
        if isinstance(B[0], list):
            lenB0 = len(B[0])
        else:
            lenB0 = 1
        if len(A[0]) != len(B):
            raise ValueError("Liczba kolumn macierzy A musi być równa liczbie wierszy macierzy B.")
        result = [[0 for _ in range(lenB0)] for _ in range(len(A))]

        if lenB0 == 1:
            for i in range(len(A)):
                for k in range(len(B)):
                    result[i][0] += A[i][k] * B[k]
            return result
        for i in range(len(A)):
            for j in range(lenB0):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        # A i B są wektorami
        if len(A) != len(B):
            raise ValueError("Długość wektorów A i B musi być taka sama.")
        result = sum([A[i] * B[i] for i in range(len(A))])
        return result
