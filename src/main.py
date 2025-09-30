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
    pass


if __name__ == "__main__":
    main()
