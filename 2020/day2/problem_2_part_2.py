"""

"""


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def validate_only_one(password, key, pos_1, pos_2):
    if password[pos_1 - 1] == key and password[pos_2 - 1] != key:
        return 1
    elif password[pos_1 - 1] != key and password[pos_2 - 1] == key:
        return 1
    else:
        return 0


def parse_password(policy, key, password):
    pos_1, pos_2 = policy.split("-")
    pos_1 = int(pos_1)
    pos_2 = int(pos_2)
    key = key[0]
    return validate_only_one(password, key, pos_1, pos_2)


def solve():
    count_valid = 0
    for line in load_file("./input.txt"):
        policy = password = ""
        policy, key, password = line.split()
        count_valid += parse_password(policy, key, password)
    print(count_valid)


solve()
