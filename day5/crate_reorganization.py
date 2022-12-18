import re
from collections import deque


def parse_crates(crates):
    sp = crates.split("\n")
    stack_nums = [int(num) for num in sp[-1].split()]
    columns = [re.split(r"\s+", row, maxsplit=len(stack_nums)) for row in sp[:-1]]
    print(columns)
    # transpose list
    stacks = [[s for s in column if s != ""] for column in list(zip(*columns))]
    # print(stacks)
    # print(stacks)
    stacks = [deque(stack) for stack in stacks]
    return stacks, stack_nums


def parse_ins(ins):
    return tuple(int(i) for i in ins)


# move n crates from from_stack to to_stack
def move_crates(stacks, n, from_stack, to_stack):
    temp = []
    for _ in range(n):
        crate = stacks[from_stack - 1].popleft()
        temp.append(crate)
    for _ in range(n):
        crate = temp.pop()
        stacks[to_stack - 1].appendleft(crate)


# run instructions on stacks
def run_instructions(instructions, stacks):
    for ins in instructions:
        move_crates(stacks, ins[0], ins[1], ins[2])


def get_stacks_string(stacks):
    return "".join(s[0][1] for s in stacks)


def parse_input(file):
    ins_regexp = r"move (\d+) from (\d+) to (\d+)"
    data = file.read().split("\n\n")
    crates = data[0]
    ins = data[1]
    all_instr = re.findall(ins_regexp, ins)
    instructions = [parse_ins(ins) for ins in all_instr]
    stacks, stack_nums = parse_crates(crates)
    return instructions, stacks, stack_nums


if __name__ == "__main__":
    with open("input.txt") as file:
        instructions, stacks, stack_nums = parse_input(file)
        stacks = [
            ["[W]", "[R]", "[T]", "[G]"],
            ["[W]", "[V ]", "[S]", "[M]", "[P]", "[H]", "[C]", "[G]"],
            ["[M]", "[G]", "[S]", "[T]", "[L]", "[C]"],
            ["[F]", "[R]", "[W]", "[M]", "[D]", "[H]", "[J]"],
            ["[J]", "[F]", "[W]", "[S]", "[H]", "[L]", "[Q]", "[P]"],
            ["[S]", "[M]", "[F]", "[N]", "[D]", "[J]", "[P]"],
            ["[J]", "[S]", "[C]", "[G]", "[F]", "[D]", "[B]", "[Z]"],
            ["[B]", "[T]", "[R]"],
            ["[C]", "[L]", "[W]", "[N]", "[H]"],
        ]
        stacks = [deque(stack) for stack in stacks]
        print(f"Before: {stacks}")
        print(stack_nums)
        run_instructions(instructions, stacks)
        print(f"After: {stacks}")
        stacks_string = get_stacks_string(stacks)
        print(f"Stacks string = {stacks_string}")
