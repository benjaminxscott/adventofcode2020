#!/usr/bin/env python3
# https://adventofcode.com/2020/day/2

'''
Given a list (your puzzle input) of passwords (according to the corrupted database) 
and the corporate policy when that password was set.

For example, suppose you have the following list:

<policy> : <pass>
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for 
the password to be valid. For example, "1-3 a" means that the password must contain "a" at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, 
but needs at least 1. The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

def main():
    with open ('day2input.txt') as fp:
        lines = fp.read().splitlines()
        num_valid:int = 0

        for line in lines:
            policy, passwd = line.split(': ')
            policy_def, policy_char = policy.split()
            min_chars, max_chars = policy_def.split('-')

            if passwd.count(policy_char) <= int(max_chars) and passwd.count(policy_char) >= int(min_chars):
                num_valid +=1

        print (num_valid)

if __name__ == '__main__':
    main()
