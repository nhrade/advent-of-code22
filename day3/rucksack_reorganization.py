from functools import reduce


def split_compartments(rucksacks):
    return [(r[: len(r) // 2], r[len(r) // 2 :]) for r in rucksacks]


def find_common_item(r1, r2):
    return next(c for c in r1 if c in set(r2))


def priority(c):
    return ord(c) - 96 if c >= "a" and c <= "z" else ord(c) - 38


def sum_all_priorities(split_rucksacks):
    return sum(priority(find_common_item(*r)) for r in split_rucksacks)


def split_into_groups(ls, n):
    return [ls[i : i + n] for i in range(0, len(ls), n)]


def find_common_item_ingroup(group):
    sets = [set(s) for s in group]
    return reduce(lambda item_set, g: item_set.intersection(g), sets).pop()


def sum_priority_groups(groups):
    return sum(priority(find_common_item_ingroup(group)) for group in groups)


with open("input.txt") as file:
    data = file.read()
    lines = data.split("\n")
    split_rucksacks = split_compartments(lines)
    total_priority = sum_all_priorities(split_rucksacks)
    print(f"total priority = {total_priority}")
    groups = split_into_groups(lines, 3)
    sum_common_priorities = sum_priority_groups(groups)
    print(f"Sum of common item priorities in groups = {sum_common_priorities}")
