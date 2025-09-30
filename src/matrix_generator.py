from random import randint, randrange

from rich.console import Console

console = Console()


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


def display(matrix: list[[int]]) -> None:  # type:ignore
    biggest_element: int = max(len(str(item)) for row in matrix for item in row)  # type:ignore
    for row in matrix:
        formatted_rows = " ".join(f"{str(item):>{biggest_element}}" for item in row)
        console.print(formatted_rows, style="bold green")


def main() -> None:
    matrix = matrix_generator(3, 3, 10, 20)
    display(matrix)


if __name__ == "__main__":
    main()
