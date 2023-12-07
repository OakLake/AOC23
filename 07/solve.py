from rich import print
from collections import Counter

TEST_CASE = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def alter_hand(hand):
    most_frequent_card = Counter(hand.replace("J", "")).most_common(1)[0][0]
    return hand.replace("J", most_frequent_card)

def five_of_kind(hand):
    f = lambda x: set(x.count(card) for card in x) == {5}
    return f(hand) or f(alter_hand(hand)) 


def four_of_kind(hand):
    f = lambda x: 4 in {x.count(card) for card in x}
    return f(hand) or f(alter_hand(hand))


def full_house(hand):
    f = lambda x: sorted([x.count(card) for card in set(x)]) == [2, 3]
    return f(hand) or f(alter_hand(hand))


def three_of_kind(hand):
    f = lambda x: sorted([x.count(card) for card in set(x)]) == [1, 1, 3]
    return f(hand) or f(alter_hand(hand))


def two_pair(hand):
    f = lambda x: sorted([x.count(card) for card in set(x)]) == [1, 2, 2]
    return f(hand) or f(alter_hand(hand))


def one_pair(hand):
    f = lambda x: sorted([x.count(card) for card in set(x)]) == [1, 1, 1, 2]
    return f(hand) or f(alter_hand(hand))


def high_card(hand):
    return len(set(hand)) == len(hand)


hand_type = {
    "FIVE_OF_KIND": five_of_kind,
    "FOUR_OF_KIND": four_of_kind,
    "FULL_HOUSE": full_house,
    "THREE_OF_KIND": three_of_kind,
    "TWO_PAIR": two_pair,
    "ONE_PAIR": one_pair,
    "HIGH_CARD": high_card,
}

hand_type_rank = {ht: 7 - ix for ix, ht in enumerate(hand_type)}

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
alpha = reversed(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"])

card_rank = {c: al for c, al in zip(cards, alpha)}

print(card_rank)


def get_hand_and_bid(line):
    splt = line.split()
    return splt[0].strip(), splt[1].strip()


def main() -> None:
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    # lines = TEST_CASE

    record = []
    for line in lines:
        hand, bid = get_hand_and_bid(line)

        for type, func in hand_type.items():
            if func(hand):
                print(f"TYPE of {hand} is: {type}")
                rank = hand_type_rank[type]
                record.append((rank, hand, bid))
                break

    print(record)

    # sorted_record = sorted(
    #     record, key=lambda x: str(x[0]) + "".join(str(card_rank[c]) for c in x[1])
    # )
    sorted_record = sorted(
        record, key=lambda x: (x[0] , "".join(card_rank[c] for c in x[1]))
    )
    print(sorted_record)

    ranked_hands = []
    for ix, record in enumerate(sorted_record):
        ranked_hands.append((ix + 1, record[1], record[2]))

    print("ranked_hands: ", ranked_hands)

    print(sum(r * int(b) for r, _, b in ranked_hands))
    # 249661501 INCORRECT ANSWER
    # 250232501 CORRECT


    # 389104726 INCORRECT TOO HIGH
    # 247910030 INCORRECT TOO LOW


if __name__ == "__main__":
    main()
