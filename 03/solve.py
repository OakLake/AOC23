from typing import List

from rich.console import Console

console = Console()

test_case = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

PERIOD = "."


def extract_matrix(lines: List[str]) -> List[List[str]]:
    period_padding: List[str] = ["." * (len(lines[0].strip()) + 2)]
    matrix = [f".{line.strip()}." for line in lines]

    return period_padding + matrix + period_padding


def solve(matrix):
    numbers_register = []

    for row_ix in range(1, len(matrix)):
        digits = ""

        for col_ix in range(1, len(matrix[0])):
            middle = matrix[row_ix][col_ix]
            if middle.isnumeric():
                digits += middle

            else:
                if digits:
                    snapshot_top = matrix[row_ix - 1][
                        col_ix - len(digits) - 1 : col_ix + 1
                    ]
                    snapshot_middle = matrix[row_ix][
                        col_ix - len(digits) - 1 : col_ix + 1
                    ]
                    snapshot_bottom = matrix[row_ix + 1][
                        col_ix - len(digits) - 1 : col_ix + 1
                    ]

                    if (
                        any(not s.isnumeric() and s != "." for s in snapshot_top)
                        or any(not s.isnumeric() and s != "." for s in snapshot_bottom)
                        or snapshot_middle[0] != "."
                        or snapshot_middle[-1] != "."
                    ):
                        numbers_register.append(int(digits))

                    digits = ""

    return numbers_register


def solve_2(matrix):
    numbers_map = {}
    star_indices = set()
    gear_ratios = 0

    for row_ix in range(1, len(matrix)):
        digits = ""

        for col_ix in range(1, len(matrix[0])):
            middle = matrix[row_ix][col_ix]
            if middle.isnumeric():
                digits += middle

            else:
                if middle == "*":
                    star_indices.add((row_ix, col_ix))

                if digits:
                    for cix in range(col_ix - len(digits), col_ix):
                        numbers_map[(row_ix, cix)] = int(digits)

                    digits = ""

    for rix, cix in star_indices:
        gears = []
        for rix_shift in [-1, 0, 1]:
            for cix_shift in [-1, 0, 1]:
                if (rix + rix_shift, cix + cix_shift) in numbers_map:
                    gear = numbers_map[rix + rix_shift, cix + cix_shift]
                    if gear not in gears:
                        gears.append(gear)

        if len(gears) == 2:
            gear_ratios += gears[0] * gears[1]
        elif len(gears) > 2:
            raise RuntimeError("Ooops!")

    return gear_ratios


def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    # lines = test_case

    padded_matrix = extract_matrix(lines)
    print(*padded_matrix, sep="\n")

    sol = solve(padded_matrix)
    print("STAGE 1: ", sum(sol))

    stage_2 = solve_2(padded_matrix)
    print("STAGE 2:", stage_2)


if __name__ == "__main__":
    main()
