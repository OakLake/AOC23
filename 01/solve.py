WORD_TO_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3, 
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_first_and_last_nums(line: str) -> int:

    line = line.strip()

    first, last = None, None
    left_p, right_p = 0, (len(line) - 1)

    while first is None or last is None:
        
        if first is None:
            if line[left_p].isnumeric():
                first = line[left_p]
            else:
                # STAGE 2 >
                for word_digit in WORD_TO_DIGIT:
                    if line[left_p:].startswith(word_digit):
                        first = WORD_TO_DIGIT[word_digit]
                        break
                # STAGE 2 <
            
            left_p += 1
        

        if last is None:
            if line[right_p].isnumeric():
                last = line[right_p]
            else:
                # STAGE 2 >
                for word_digit in WORD_TO_DIGIT:
                    if line[right_p:].startswith(word_digit):
                        last = WORD_TO_DIGIT[word_digit]
                        break
                # STAGE 2 <
            
            right_p -= 1



    return int(f"{first}{last}")


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    
    sum_ = sum(get_first_and_last_nums(line) for line in lines)

    print(sum_)


main()