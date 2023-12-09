from collections import deque
import sys
from rich import print

sys.setrecursionlimit(20000)

NAV = "LRRLLRLRRRLRRRLRRLRRRLRRLRRRLRRLRRRLRLRRRLRRRLRRRLRLRRLRRRLRRRLRRLRRLRRLRLLLRRRLRRRLRLRLRRLLRRRLRRLRRRLRLRRLRRRLRRRLLRLRLLRRRLRRRLLRRRLRRRLRRRLRRLRRRLLLRRRLRLLLRLRLRLLRLRLLLRRLRRLLRRLRRRLRRLRRLRLRRLLRRLRLRRLLLRRRLLRRRLLRLRLLRRRLRLLRRLRLRRLRLRRRLLRRRLLRRLRLRRLRRLLRLRLRRRLRLRRRR"


TEST_CASE_NAV_1 = "RL"
TEST_CASE_LINES_1 = [
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

TEST_CASE_NAV_2 = "LLR"
TEST_CASE_LINES_2 = [
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]


class Node:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


def extract_directions(line):
    splt = line.split("=")
    curr = splt[0].strip()

    des = splt[1].replace("(", "").replace(")", "").split(",")
    left, right = des[0].strip(), des[1].strip()

    return [curr, left, right]


def mapify(lines):
    map_ = {}
    for l in lines:
        curr, left, right = extract_directions(l)
        map_[curr] = (left, right)
    return map_


def solve(lines_, nav_) -> None:
    desert_map = mapify(lines_)

    def dfs(curr, path, nav, i):
        nonlocal desert_map

        if curr == "ZZZ":
            return path

        next_nav = nav_[i%len(nav)]
        i += 1

        next_node = desert_map[curr][next_nav == "R"]

        print(f"From {curr} Take: {next_nav} To {next_node}, REF: {desert_map[curr]}")

        r = dfs(next_node, path + [curr], nav, i)
        if r is not None:
            return r

        return None

    z_path = dfs("AAA", [], nav_, 0)
    print(len(z_path))
        


def main():
    with open("./input.txt", "r") as f:
        l = f.readlines()
        n = NAV

    # l, n = TEST_CASE_LINES_1, TEST_CASE_NAV_1
    # l, n = TEST_CASE_LINES_2, TEST_CASE_NAV_2

    r = solve(l, n)
    print(r)


if __name__ == "__main__":
    main()


# 14681