from matrix_generator import display, matrix_generator


def factorisation(U):
    ## creating pre L matrix
    n = len(U)

    L_form = []

    for i in range(n):
        temp_row = []

        for j in range(n):
            if i == j:
                temp_row.append(1)
            else:
                temp_row.append(0)
        L_form.append(temp_row)

    for i in range(n):
        for j in range(i + 1, n):
            m = round(U[j][i] / U[i][i], 2)
            L_form[j][i] = m
            for k in range(i, n):
                U[j][k] = round(U[j][k] - m * U[i][k], 2)

    # print("L matrix :\n")
    # for i in l:
    #     print(i)
    # print("\n")
    # print("U matrix :\n")

    # for i in U:
    #     print(i)

    print("L matrix form: ")
    display(L_form)
    print("U_form")
    display(U)


def main() -> None:
    A = []
    size = int(input("Enter the size of the matrix: "))
    for i in range(size):
        temp = []
        for j in range(size):
            print(f"Enter {j + 1} element of {i + 1} row")
            temp.append(int(input()))
        A.append(temp)

    factorisation(A)


if __name__ == "__main__":
    main()
