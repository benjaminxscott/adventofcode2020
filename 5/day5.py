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

--
Part 2:
It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

import math
from collections import Counter

def parse_binary_map(in_string):
    # zero-based indices
    highest_value = 2 ** len(in_string) -1
    lowest_value = 0
    for i, char in enumerate(in_string):
        if char in ('R', 'B'):
            # move our "lowest possible row" up by half of the remaining rows
            lowest_value += math.ceil((highest_value - lowest_value) / 2)
        elif char in ('L', 'F'):
            # move our "highest possible row" down by half of itself
            highest_value -= math.ceil((highest_value  - lowest_value )/ 2)
        else:
            raise Exception
        #print(f"char at {i} is:{char}, possible rows:{lowest_value} to {highest_value}")

    return lowest_value

def main():
    with open ('day5input.txt') as fp:
        lines = fp.read().splitlines()
        seats = Counter()

        highest_seat_id = 0

        for line in lines:
            row = parse_binary_map(line[:7])
            col = parse_binary_map(line[7:])
            seat_id = row * 8 + col

            # keep track of which seats are taken
            seats[seat_id] = 1
            highest_seat_id = max(highest_seat_id, seat_id)

        # find the seat ID that is not contiguous (e.g. we may have seats 0-100 not taken, seats 101 to 1000 taken, and seat 999 open)
        # so we keep track of which seat IDs have been observed, and see if its 'neighbors' are taken (via pigeonhole principle this must be the only open seat)
        open_seat = -1
        for i in range (2**len(lines)):
            if not seats[i] and seats[i-1] and seats[i+1]:
                open_seat = i
                break
        print(f"open seat is: {open_seat}")
        print(f"highest seatID is: {highest_seat_id}")
if __name__ == '__main__':
    main()
