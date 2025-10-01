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


def factorisation(U_form):
    ## creating pre L matrix
    n = len(U_form)

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
            m = round(U_form[j][i] / U_form[i][i], 2)
            L_form[j][i] = m
            for k in range(i, n):
                U_form[j][k] = round(U_form[j][k] - m * U_form[i][k], 2)

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
    display(U_form)


def main() -> None:
    matrix: list[[float]] = custom_matrix()  # type:ignore
    factorisation(matrix)


if __name__ == "__main__":
    main()
