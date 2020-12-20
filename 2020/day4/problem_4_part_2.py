"""

"""
import re


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def validate_passport(passport):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    all_present_and_valid = 1
    for key in passport:
        if passport[key] == "":
            print("missing " + key)
            return 0
        else:
            if key == "byr":
                # 4 digits / 1920 - 2002
                val = int(passport[key])
                if not (val >= 1920 and val <= 2002):
                    all_present_and_valid = 0

            elif key == "iyr":
                # 4 digits / 2010 - 2020
                val = int(passport[key])
                if not (val >= 2010 and val <= 2020):
                    all_present_and_valid = 0

            elif key == "eyr":
                # 4 digits / 2020 - 2030
                val = int(passport[key])
                if not (val >= 2020 and val <= 2030):
                    all_present_and_valid = 0

            elif key == "hgt":
                # cm: 150 - 193 || in: 59 - 76
                if "cm" in passport[key]:
                    val = int(passport[key].split("cm")[0])
                    if not (val >= 150 and val <= 193):
                        all_present_and_valid = 0
                elif "in" in passport[key]:
                    val = int(passport[key].split("in")[0])
                    if not (val >= 59 and val <= 76):
                        all_present_and_valid = 0
                else:
                    all_present_and_valid = 0

            elif key == "hcl":
                # a # followed by exactly six characters 0-9 or a-f
                pattern = r"^\#[0-9a-f]{6}$"
                result = re.match(pattern, passport[key])
                if not result:
                    all_present_and_valid = 0

            elif key == "ecl":
                # exactly one of: amb blu brn gry grn hzl oth
                allowed_vals = [
                    "amb",
                    "blu",
                    "brn",
                    "gry",
                    "grn",
                    "hzl",
                    "oth",
                ]
                if passport[key] not in allowed_vals:
                    all_present_and_valid = 0

            elif key == "pid":
                # a nine-digit number, including leading zeroes.
                pattern = r"^\d{9}$"
                result = re.match(pattern, passport[key])
                if not result:
                    all_present_and_valid = 0

    return all_present_and_valid


def get_passport():
    passport = {}
    valid_passports = 0
    for line in load_file("./input.txt"):
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
        else:
            row = line.split(" ")
            for item in row:
                key, value = item.split(":")
                # print("Key: " + key)
                # print("Value: " + value)
                passport[key] = value.split("\n")[0]

    return valid_passports


def solve():
    print(get_passport())


solve()
