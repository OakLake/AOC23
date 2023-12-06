from typing import List


TEST_LINES = [
    "Time:      7  15   30",
    "Distance:  9  40  200"
]



def get_numbers_part_1(line: str) -> List[int]:
    return [int(n) for n in line.split(":")[1].strip().split()]


def get_numbers_part_2(line: str) -> int:
    return [int("".join(str(n) for n in get_numbers_part_1(line)))]

def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    
    # lines = TEST_LINES


    race_times = get_numbers_part_2(lines[0])
    race_distances = get_numbers_part_2(lines[1])

    mul = 1
    for race_time, race_distance in zip(race_times, race_distances):
        print(f"race_time: {race_time}, race_distance: {race_distance}")
        ways = 0
        for speed in range(1, race_time):
            time_left = race_time - speed
            distance = speed * time_left

            if time_left <= race_time and distance > race_distance:
                print(f"time_left: {time_left} vs {race_time}, distance: {distance} >= {race_distance}")
                ways += 1
        
        if ways:
            print(ways)
            mul *= ways 
    
    print(mul)


if __name__ == "__main__":
    main()
