# Turns out you get greeted with this message:
# Puzzle inputs differ by user.  Please log in to get your puzzle input.
# which is pretty cool :)
# might look later at cookie or something, just use browser and copy for now
"""
import requests

def get_puzzle():
    resp = requests.get("https://adventofcode.com/2020/day/3/input")
    print(resp.content)

get_puzzle()
"""

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


def traverse_puzzle(puzzle):
    cur_row = cur_col = new_col = hit_tree = 0

    while cur_row < len(puzzle) - 1:
        # print(puzzle[cur_row][cur_col])
        row_length = len(puzzle[cur_row + 1])  # 31

        try:
            new_col += 3
            if new_col >= row_length:
                new_col = new_col - row_length

            if puzzle[cur_row + 1][new_col] == TREE:
                hit_tree += 1

        except IndexError as e:
            print(new_col)

        cur_row += 1
        cur_col = new_col

    return hit_tree


def solve():
    puzzle = load_puzzle_into_list()

    # for row in puzzle:
    #    print(row)

    num_of_trees = traverse_puzzle(puzzle)
    print(num_of_trees)


solve()
