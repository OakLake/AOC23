from collections import defaultdict
from typing import Tuple

RED_CUBES_NUM = 12
GREEN_CUBES_NUM = 13
BLUE_CUBES_NUM = 14

RED, GREEN, BLUE = "red", "green", "blue"


def parse_game(line: str) -> Tuple[int, int, int, int]:
    game, game_sets = line.split(":")

    game_id = int(game.split()[1])

    cubes_counter = defaultdict(lambda: 0)
    for cubes_drawn in game_sets.split(";"):
        for draw in cubes_drawn.split(","):
            count, colour = draw.split()
            cubes_counter[colour] = max(cubes_counter[colour], int(count))

    return game_id, cubes_counter[RED], cubes_counter[GREEN], cubes_counter[BLUE]


def is_game_possible(reds, greens, blues) -> bool:
    return all(
        [reds <= RED_CUBES_NUM, greens <= GREEN_CUBES_NUM, blues <= BLUE_CUBES_NUM]
    )


def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    sum_possible_game_ids = 0
    sum_powers = 0
    
    for line in lines:
        game_id, reds, greens, blues = parse_game(line)

        if is_game_possible(reds, greens, blues):
            sum_possible_game_ids += game_id

        sum_powers += reds * greens * blues

    print("PART 1: ", sum_possible_game_ids)
    print("PART 2: ", sum_powers)


if __name__ == "__main__":
    main()
