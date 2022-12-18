def move_head(head_pos, dir):
    if dir == "L":
        head_pos = (head_pos[0], head_pos[1] - 1)
    elif dir == "R":
        head_pos = (head_pos[0], head_pos[1] + 1)
    elif dir == "U":
        head_pos = (head_pos[0] - 1, head_pos[1])
    elif dir == "D":
        head_pos = (head_pos[0] + 1, head_pos[1])
    return head_pos


def move_tail(tail_pos, head_pos):
    xdir = head_pos[0] - tail_pos[0]
    ydir = head_pos[1] - tail_pos[1]
    xnorm = xdir / abs(xdir) if abs(xdir) > 0 else 0
    ynorm = ydir / abs(ydir) if abs(ydir) > 0 else 0

    if abs(xdir) == 2:
        tail_pos = (tail_pos[0] + xnorm, tail_pos[1])
    elif abs(ydir) == 2:
        tail_pos = (tail_pos[0], tail_pos[1] + ynorm)
    else:
        tail_pos = (tail_pos[0] + xnorm, tail_pos[1] + ynorm)
    return tail_pos


def print_rope(tail, head, size):
    for r in range(size[0]):
        for c in range(size[1]):
            if (r, c) == head:
                print("H", end="")
            elif (r, c) == tail:
                print("T", end="")
            else:
                print(".", end="")
        print()
    print()


def run_ins(instr, init_head, init_tail):
    head = init_head
    tail = init_tail
    head_positions = [head]
    tail_positions = [tail]
    print_rope(tail, head, (5, 6))
    for ins in instr:
        ls = ins.split(" ")
        amount = int(ls[1])
        print(f"===    {ins}   ===\n")
        for _ in range(amount):
            head = move_head(head, ls[0])
            head_positions.append(head)
            tail_positions.append(tail)
            print_rope(tail, head, (5, 6))
            tail = move_tail(tail, head)
    return head_positions, tail_positions


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        head_pos = (4, 0)
        tail_pos = (4, 0)

        head_positions, tail_positions = run_ins(lines, head_pos, tail_pos)
