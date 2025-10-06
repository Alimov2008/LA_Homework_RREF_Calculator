from matrix_generator import display, matrix_generator
from RREF_solver import factorisation


def get_int(context: str) -> int:
    while True:
        try:
            temp = int(input(context))
        except ValueError:
            print("Input only numbers")
            continue
        break
    return temp


def main() -> None:
    matrix_size_x: int = get_int("Enter X size of matrix : ")
    matrix_size_y: int = get_int("Enter Y size of matrix : ")
    min_key_value: int = get_int("Enter minimum value of elements : ")
    max_key_value: int = get_int("Enter max value of elements : ")
    matrix: list[[int]] = matrix_generator(  # type:ignore
        matrix_size_x, matrix_size_y, min_key_value, max_key_value
    )
    print("\nInputted matrix : \n")
    display(matrix)
    answer = factorisation(matrix)
    display(answer)


if __name__ == "__main__":
    main()
