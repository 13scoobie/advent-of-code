"""
Solution for Day 1, Part 1
Author: David White
Date: 01-18-2018
"""

def solve():
    current_floor = 0
    with open('input.txt', 'r') as input:
        for char in input:
            for stair in range(0, len(char)):
                if(char[stair] == '('):
                    current_floor += 1
                elif(char[stair] == ')'):
                    current_floor -= 1
    print(current_floor)
    return

if __name__ == "__main__":
    solve()
