"""
Solution for Day 2, Part 1
Author: David White
Date: 01-18-2018
"""

def solve():
    feet_of_paper = 0
    with open('input.txt', 'r') as input:
        for char in input:
            surface_area = 0
            l, w, h = char.strip().split('x')
            l, w, h = int(l), int(w), int(h)
            surface_area = (2*l*w + 2*w*h + 2*h*l)
            a, b, c = l*w, w*h, h*l
            extra_paper = min(a, b, c)
            feet_of_paper += surface_area + extra_paper
    return feet_of_paper

if __name__ == "__main__":
    print(solve())


