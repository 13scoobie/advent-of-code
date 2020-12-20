"""
"""


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def part_two():
    all_questions_answered = 0
    group = {}
    number_of_people_in_group = 0
    for line in load_file("input.txt"):
        # print(line)
        number_of_people_in_group += 1
        for char in line.rstrip():
            if line:
                if char in group:
                    group[char] = group[char] + 1
                else:
                    group.update({char: 1})

        if line == "\n":
            number_of_people_in_group -= 1
            for questions_answered in group:
                if group[questions_answered] == number_of_people_in_group:
                    all_questions_answered += 1

            group = {}
            number_of_people_in_group = 0

    for questions_answered in group:
        if group[questions_answered] == number_of_people_in_group:
            all_questions_answered += 1

    return all_questions_answered


def calculate_questions_answered():
    questions_answered = 0
    group = set()
    for line in load_file("input.txt"):
        # print(line)
        for char in line.rstrip():
            if line:
                group.add(char)

        if line == "\n":
            questions_answered += len(group)
            group = set()

    questions_answered += len(group)
    return questions_answered


def solve():
    print(calculate_questions_answered())
    print(part_two())


solve()