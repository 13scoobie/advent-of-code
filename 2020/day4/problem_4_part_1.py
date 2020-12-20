"""

"""


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def validate_passport(passport):
    return 0 if any(value == "" for value in passport.values()) else 1


def get_passport():
    passport = {}
    valid_passports = 0
    for line in load_file("./input.txt"):
        row = line.split(" ")
        # print(row)
        if row[0] != "\n":
            for item in row:
                key, value = item.split(":")
                passport[key] = value.split("\n")[0]

        if line == "\n":
            # print("new passport \n\n")
            # print(passport)
            valid_passports += validate_passport(passport)
            from pprint import pprint

            pprint(passport)
            print("\n")

            # reset
            passport = {
                "byr": "",
                "iyr": "",
                "eyr": "",
                "hgt": "",
                "hcl": "",
                "ecl": "",
                "pid": ""
                # "cid": "",
            }

    return valid_passports


def solve():
    print(get_passport())


solve()
