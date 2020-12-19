TREE = "#"
PATH = "."


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def load_puzzle_into_list():
    grid = []
    for idx, line in enumerate(load_file("./input.txt")):
        grid.append([char for char in line if char != "\n"])

    return grid


def traverse_puzzle(puzzle, *params):
    right_step = params[0]
    down_step = params[1]

    cur_row = cur_col = new_col = hit_tree = 0

    while cur_row < len(puzzle) - 1:
        # print(puzzle[cur_row][cur_col])
        row_length = len(puzzle[cur_row + 1])  # 31

        try:
            new_col += right_step
            if new_col >= row_length:
                new_col = new_col - row_length

            if puzzle[cur_row + down_step][new_col] == TREE:
                hit_tree += 1

        except IndexError as e:
            print(new_col)

        cur_row += down_step
        cur_col = new_col

    return hit_tree


def solve():
    puzzle = load_puzzle_into_list()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for slope in slopes:
        product *= traverse_puzzle(puzzle, *slope)
    print(product)


solve()
