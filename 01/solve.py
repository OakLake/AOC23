from typing import Optional


WORD_TO_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_number(line: str, index: int) -> Optional[bool]:
    number = None

    if line[index].isnumeric():
        number = line[index]
    else:
        # STAGE 2 >
        for word_digit in WORD_TO_DIGIT:
            if line[index:].startswith(word_digit):
                number = WORD_TO_DIGIT[word_digit]
                break
        # STAGE 2 <

    return number


def get_first_and_last_nums(line: str) -> int:
    line = line.strip()

    first, last = None, None
    left_p, right_p = 0, (len(line) - 1)

    while first is None or last is None:
        if first is None:
            extracted_number = extract_number(line, left_p)
            if extracted_number is not None:
                first = extracted_number

            left_p += 1

        if last is None:
            extracted_number = extract_number(line, right_p)
            if extracted_number is not None:
                last = extracted_number

            right_p -= 1

    return int(f"{first}{last}")


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    sum_ = sum(get_first_and_last_nums(line) for line in lines)

    print(sum_)


main()
