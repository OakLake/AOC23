
import os

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


def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    # lines = test_case

    padded_matrix = extract_matrix(lines)
    print(*padded_matrix, sep="\n")
    
    sol = solve(padded_matrix)
    # print(sol)
    
    print("STAGE 1: ", sum(sol))


if __name__ == "__main__":
    main()
