from random import randint, randrange


def get_random_number(min_value: int, max_value: int) -> int:
    return randrange(min_value, max_value)


def matrix_generator(
    size_x: int, size_y: int, min_value: int, max_value: int
) -> list[[int]]:  # type: ignore
    matrix: list[[int]] = []  # type: ignore

    for i in range(size_x):
        row: list = []
        for i in range(size_y):
            row.append(get_random_number(min_value, max_value))
        matrix.append(row)
    return matrix


def main() -> None:
    print(matrix_generator(3, 3, 10, 20))


if __name__ == "__main__":
    main()
