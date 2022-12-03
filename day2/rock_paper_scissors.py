# checks who wins returns 1 for first player 2 for second and 0 for draw
def who_wins(p1, p2):
    n1 = ord(p1) - 65
    n2 = ord(p2) - 88
    if n1 == n2:
        return 0
    return 1 if (n1 - 1) % 3 == n2 else 2


# calc score for two players
def calc_score(p1, p2):
    scoring_table = {1: 0, 2: 6, 0: 3}
    return scoring_table[who_wins(p1, p2)] + (ord(p2) - 87)


# calc total score
def calc_total_score(strategy):
    return sum(calc_score(p1, p2) for p1, p2 in strategy)


# calc the best move depending on the outcome desired.
def calc_move(p, outcome):
    opponent_move = ord(p) - 65
    # lose
    if outcome == "X":
        return chr((opponent_move - 1) % 3 + 88)
    # draw
    elif outcome == "Y":
        return chr(opponent_move + 88)
    # win
    elif outcome == "Z":
        return chr((opponent_move + 1) % 3 + 88)


# calculate new total score after picking moves
def calc_new_total_score(old_strategy):
    new_strategy = [(s[0], calc_move(s[0], s[1])) for s in old_strategy]
    return calc_total_score(new_strategy)


with open("input.txt") as file:
    text = file.read()
    lines = text.split("\n")
    strategy = [line.split(" ") for line in lines]
    print(f"Total score = {calc_total_score(strategy)}")
    print(f"New total score = {calc_new_total_score(strategy)}")
