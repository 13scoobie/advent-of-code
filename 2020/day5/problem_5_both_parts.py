"""

"""


def load_file(filename):
    for row in open(filename, "r"):
        yield row


def find_row_binary(row):
    row = row.replace("B", "1")
    row = row.replace("F", "0")
    row_number = int(row, 2)
    return row_number


def find_seat_binary(seat):
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")
    seat_number = int(seat, 2)
    return seat_number


def process_boardpass(boarding_pass):
    row = boarding_pass[:7]
    seat = boarding_pass[7:]

    final_row = find_row_binary(row)
    final_seat = find_seat_binary(seat)
    seat_id = (final_row * 8) + final_seat
    # print("row {}, column {}, seat ID {}".format(final_row, final_seat, seat_id))
    return seat_id


def solve():
    boardpass_list = []
    for line in load_file("input.txt"):
        boarding_pass = line
        seat_id = process_boardpass(boarding_pass)
        boardpass_list.append(seat_id)
    boardpass_list.sort()
    for idx, seat in enumerate(boardpass_list):
        # print("index: {}, seat_id: {}".format(idx, seat))
        seat = [
            x
            for x in range(boardpass_list[0], boardpass_list[-1] + 1)
            if x not in boardpass_list
        ]

    print(boardpass_list[-1:])
    print(seat)


solve()
