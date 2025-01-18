#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2#part2

"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one (XOR) of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""


def main():
    with open("day2input.txt") as fp:
        lines = fp.read().splitlines()
        num_valid = 0

        for line in lines:
            policy, passwd = line.split(": ")

            policy_def, policy_char = policy.split()
            indices = policy_def.split("-")
            index_1, index_2 = [min(int(x) - 1, 0) for x in indices]
            print(f"Checking for zero-based indices: {index_1}, {index_2} in {passwd}")

            # XOR on whether the char(s) at given index is correct
            if bool(passwd[index_1] == policy_char) ^ bool(
                passwd[index_2] == policy_char
            ):
                num_valid += 1
    # DONE
    print(num_valid)


if __name__ == "__main__":
    main()
