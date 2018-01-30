"""
Solution for Day 3, Part 1
Author: David White
Date: 01-20-2018
"""


def solve():
    with open('input_1.txt', 'r') as input:
        for map in input:
            location = [0,0]
            visited_location = []
            visited_location.append(location[:])

            total_house_count = 1
            unique_house_count = 1
            number_of_houses = 0

            for direction in map:
                if direction == '^':
                    #print "North"
                    location[0] += 1
                if direction == "v":
                    #print "South"
                    location[0] -= 1
                if direction == ">":
                    #print "East"
                    location[1] += 1
                if direction == "<":
                    #print "West"
                    location[1] -= 1
                
                if location in visited_location:
                    number_of_houses += 1
                else:
                    unique_house_count += 1
                total_house_count += 1
                visited_location.append(location[:])

            print("Total Visits: "+str(total_house_count))
            print("Number of duplicate houses: "+str(number_of_houses))
            print("Unique Houses: "+str(unique_house_count))
                
    return


if __name__ == "__main__":
    solve()

