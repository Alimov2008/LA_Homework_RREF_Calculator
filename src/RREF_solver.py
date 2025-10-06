from matrix_generator import display, matrix_generator


def custom_matrix() -> list[[float]]:  # type:ignore
    custom_matrix = []
    size = int(input("Enter the size of the matrix: "))
    for i in range(size):
        temp = []
        for j in range(size):
            print(f"Enter {j + 1} element of {i + 1} row")
            temp.append(float(input()))
        custom_matrix.append(temp)
    return custom_matrix


def factorisation(A):
    n = len(A)

    # Create deep copy of A to avoid modifying input
    A = [row[:] for row in A]

    # Initialize matrices
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    # Identity matrix
    P = [[float(i == j) for j in range(n)] for i in range(n)]

    for i in range(n):
        # Partial Pivoting: find pivot row
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[max_row][i]) < 1e-12:
            raise ValueError("Matrix is singular or near-singular!")

        # Swap rows in A and P
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            P[i], P[max_row] = P[max_row], P[i]
            L[i][:i], L[max_row][:i] = L[max_row][:i], L[i][:i]

        # U matrix
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_val

        # L matrix
        for k in range(i + 1, n):
            sum_val = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_val) / U[i][i]

        L[i][i] = 1.0
    L = [[round(val, 3) for val in row] for row in L]
    U = [[round(val, 3) for val in row] for row in U]
    P = [[round(val, 3) for val in row] for row in P]

    return P, L, U


def main() -> None:
    matrix: list[[float]] = custom_matrix()  # type:ignore
    P, L, U = factorisation(matrix)
    display(P)
    display(L)
    display(U)


if __name__ == "__main__":
    main()
