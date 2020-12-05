from typing import List
from math import floor

# Notes
# - First 7 characters specify the rows.
# - Rows go from 0 to 127


def row_and_column_finder(
        seat: str, rows: int = 128, cols: int = 8, row_lower: str = 'F', row_upper: str = 'B', col_lower: str = 'L', col_upper: str = 'R') -> List[int]:
    # This method takes a seat identifier string and gives you the
    # row and column number of the seat.
    row_lower_bound = 0
    row_upper_bound = rows
    row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2)

    row_lower_half = [row_lower_bound, row_number]
    row_upper_half = [row_number, row_upper_bound]

    col_lower_bound = 0
    col_upper_bound = cols
    col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2)

    col_lower_half = [col_lower_bound, col_number]
    col_upper_half = [col_number, col_upper_bound]

    for code in seat:

        if code == row_lower:

            row_lower_bound = row_lower_half[0]  # 0
            row_upper_bound = row_lower_half[1]  # 64
            # This is the middle point
            row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2)
            row_lower_half = [row_lower_bound, row_number]
            row_upper_half = [row_number, row_upper_bound]

        elif code == row_upper:

            row_lower_bound = row_upper_half[0]
            row_upper_bound = row_upper_half[1]
            # This is the middle point
            row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2)
            row_lower_half = [row_lower_bound, row_number]
            row_upper_half = [row_number, row_upper_bound]

        elif code == col_lower:

            col_lower_bound = col_lower_half[0]
            col_upper_bound = col_lower_half[1]
            # This is the middle point
            col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2)
            col_lower_half = [col_lower_bound, col_number]
            col_upper_half = [col_number, col_upper_bound]

        elif code == col_upper:

            col_lower_bound = col_upper_half[0]
            col_upper_bound = col_upper_half[1]
            # This is the middle point
            col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2)
            col_lower_half = [col_lower_bound, col_number]
            col_upper_half = [col_number, col_upper_bound]

        # print(row_number, col_number) Debugging

    return [row_number, col_number]


def get_seat_id(row_col: List[int]) -> int:

    row = row_col[0]
    col = row_col[1]

    seat_id = (row * 8) + col

    return seat_id


# Part 1
# Test cases --------------------------------------------
test_input_pt1 = open('5_one_test.txt', 'r').readlines()
test_input_pt1 = [x.strip() for x in test_input_pt1]

test_input_pt1

for seat in test_input_pt1:
    result = row_and_column_finder(seat)
    seat_id = get_seat_id(result)
    print(result, seat_id)

# Input --------------------------------------------

input_pt1 = open('5_pt1_input.txt', 'r').readlines()
input_pt1 = [x.strip() for x in input_pt1]

seat_ids = []
for seat in input_pt1:
    result = row_and_column_finder(seat)
    seat_id = get_seat_id(result)
    seat_ids.append(seat_id)

max(seat_ids)
