from collections import defaultdict
from typing import List, Tuple

TEST_CASE = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def extract_numbers(line: str) -> Tuple[List[int], List[int]]:
    winning, own = line.split(":")[1].strip().split("|")
    winning = [int(n) for n in winning.strip().split()]
    own = [int(n) for n in own.strip().split()]

    return winning, own


def calculate_matching_numbers(winning: List[int], own: List[int]) -> int:
    return sum([wn in winning for wn in own])


def calculate_winning_score(winning: List[int], own: List[int]) -> int:
    winners = [wn in winning for wn in own]
    return 2 ** (sum(winners) - 1) if sum(winners) else 0


def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    # lines = TEST_CASE

    scratch_card_multiplier = defaultdict(lambda: 1)

    sum_ = 0
    for card_num, line in enumerate(lines):
        winning, own = extract_numbers(line)

        score = calculate_winning_score(winning, own)
        sum_ += score

        matching = calculate_matching_numbers(winning, own)

        card_num += 1
        for _ in range(scratch_card_multiplier[card_num]):
            for cix in range(matching):
                scratch_card_multiplier[card_num + cix + 1] += 1

    print("STAGE 1: ", sum_)
    print("STAGE 2: ", sum(scratch_card_multiplier.values()))


if __name__ == "__main__":
    main()
