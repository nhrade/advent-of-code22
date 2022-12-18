import numpy as np
import itertools


def parse_data(data):
    data = data.splitlines()
    arr = np.zeros((len(data), len(data[0])), dtype=np.int32)
    for r in range(len(data[0])):
        for c in range(len(data[1])):
            arr[r, c] = int(data[r][c])
    return arr


# is tree at r, c visible
def is_visible(trees, r, c):
    return (
        r == 0
        or c == 0
        or r == trees.shape[0] - 1
        or c == trees.shape[0] - 1
        or np.all(trees[r, :c] < trees[r, c])
        or np.all(trees[r, c + 1 :] < trees[r, c])
        or np.all(trees[:r, c] < trees[r, c])
        or np.all(trees[r + 1 :, c] < trees[r, c])
    )


def scenic_score(trees, r, c):
    up = down = left = right = 0
    # up direction
    for k in range(r - 1, -1, -1):
        if trees[k, c] >= trees[r, c]:
            up += 1
            break
        up += 1
    # down direction
    for k in range(r + 1, trees.shape[0]):
        if trees[k, c] >= trees[r, c]:
            down += 1
            break
        down += 1
    # left direction
    for k in range(c - 1, -1, -1):
        if trees[r, k] >= trees[r, c]:
            left += 1
            break
        left += 1
    # right direction
    for k in range(c + 1, trees.shape[1]):
        if trees[r, k] >= trees[r, c]:
            right += 1
            break
        right += 1

    print(up, down, left, right)
    return up * down * left * right


def max_scenic_score(forest):
    # Keep track of the maximum scenic score seen so far
    max_score = 0
    for r, c in itertools.product(range(forest.shape[0]), range(forest.shape[1])):
        score = scenic_score(trees, r, c)
        if score > max_score:
            max_score = score
    return max_score


def count_visible(trees):
    return int(
        sum(
            is_visible(trees, r, c)
            for r, c in itertools.product(range(trees.shape[0]), range(trees.shape[1]))
        )
    )


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read()
        trees = parse_data(data)
        count = count_visible(trees)
        print(f"Count is {count}")
        max_score = max_scenic_score(trees)
        print(f"Max scenic score is {max_score}")
