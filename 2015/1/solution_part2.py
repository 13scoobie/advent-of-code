"""
Solution for Day 1, Part 2
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
		if(current_floor == -1):
		    return stair+1 #add one stair for starting at position 1
    return None

if __name__ == "__main__":
    print(solve())
