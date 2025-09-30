from matrix_generator import display, matrix_generator


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
    matrix: list[[int]] = matrix_generator(
        matrix_size_x, matrix_size_y, min_key_value, max_key_value
    )
    display(matrix)


if __name__ == "__main__":
    main()
