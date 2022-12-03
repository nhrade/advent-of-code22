from functools import reduce


def find_highest_calories(calories):
    return reduce(max, calories)


def find_top_three(calories):
    return sorted(calories, reverse=True)[:3]


with open("input.txt") as file:
    text = file.read()
    blocks = text.split("\n\n")
    calories = [[int(s) for s in block.split("\n")] for block in blocks]
    total_calories = [sum(c) for c in calories]
    print(f"Highest calories = {find_highest_calories(total_calories)}")
    top_three = find_top_three(total_calories)
    print(f"Sum of top three calories = {sum(top_three)}")
