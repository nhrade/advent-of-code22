import re
from dataclasses import dataclass

@dataclass
class Interval:
    left: int
    right: int

    def __lt__(self, other):
        return self.right < other.left

    def __gt__(self, other):
        return self.left > other.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __contains__(self, key):
        return self.left <= key.left and self.right >= key.right

    def overlap(self, other):
        return self >= other and self <= other

    def __repr__(self):
        return f"({self.left}, {self.right})"


def read_assignments(file):
    pattern = r"(\d+)-(\d+),(\d+)-(\d+)"
    lines = re.findall(pattern, file.read())
    return [
        (Interval(int(a[0]), int(a[1])), Interval(int(a[2]), int(a[3]))) for a in lines
    ]


def count_containing_pairs(assignments):
    return sum(a in b or b in a for a, b in assignments)


def count_overlapping(assignments):
    return sum(not (a > b or a < b) for a, b in assignments)


with open("input.txt") as file:
    assignments = read_assignments(file)
    count_containing = count_containing_pairs(assignments)
    print(f"Total number of containing pairs = {count_containing}")
    count_overlapping = count_overlapping(assignments)
    print(f"Total number of overlapping pairs = {count_overlapping}")
