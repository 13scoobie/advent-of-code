"""

"""


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def parse_password(policy, key, password):
    policy_min, policy_max = policy.split("-")
    key = key[0]
    keys_per_password = find(password, key)
    print(
        "{} found {} times. expected between {} and {}".format(
            key, len(keys_per_password), policy_min, policy_max
        )
    )
    if len(keys_per_password) >= int(policy_min) and len(keys_per_password) <= int(
        policy_max
    ):
        return 1
    else:
        return 0


def solve():
    count_valid = 0
    for line in load_file("./input.txt"):
        policy = password = ""
        policy, key, password = line.split()
        count_valid += parse_password(policy, key, password)
    print(count_valid)


solve()
