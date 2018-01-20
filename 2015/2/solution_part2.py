"""
Solution for Day 2, Part 2
Author: David White
Date: 01-18-2018
"""

def solve():
    feet_of_ribbon = 0
    with open('input.txt', 'r') as input:
        for char in input:
            l, w, h = char.strip().split('x')
            l, w, h = int(l), int(w), int(h)
            present_ribbon = 2 * min(l+w, w+h, l+h)
            bow_ribbon = (l * w * h)
            feet_of_ribbon += present_ribbon + bow_ribbon 
    return feet_of_ribbon

if __name__ == "__main__":
    print(solve())


