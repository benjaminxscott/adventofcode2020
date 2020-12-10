#!/usr/bin/env python3
# https://adventofcode.com/2020/day/5

'''
A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
Each letter tells you which half of a region the given seat is in. Start with the whole list of rows;
the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127).

The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.

The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps.
L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
'''

import math

def main():
    with open ('day5input.txt') as fp:
        # TODO - grabbing zeroth for testing
        lines = [fp.read().splitlines()[0]]

        # zero-based indices
        back_row = 127
        right_col = 7
        highest_seat_id = 0

        # split the first 8 digits of our input row
        lines = ['FBFBBFFRLR']
        for line in lines:
            print (line)
            highest_row = back_row
            lowest_row = 0
            highest_col = right_col
            lowest_col = 0
            for i in range(math.ceil(math.log(back_row, 2))):
                # we assume that input is sane, and is only "B(ack)" or "F(ront)"
                if line[i] == "B":
                    lowest_row = math.ceil(highest_row / 2)
                else:
                    highest_row = math.floor(highest_row / 2)
                print(f"char at {i} is:{line[i]}, possible rows:{lowest_row} to {highest_row}")

if __name__ == '__main__':
    main()
