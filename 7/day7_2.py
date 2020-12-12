#!/usr/bin/env python3
# https://adventofcode.com/2020/day/7

'''
Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
'''

import re
from collections import defaultdict

def find_target(target):
    count = 1
    for rule in RULES[target]:
        multiplier = RULES[target][rule]
        count += multiplier * find_target(rule)
    return count


def main():
    with open ('day7input.txt') as fp:
        lines = fp.read().splitlines()
        # symbols always have two adjectives, numbers don't matter
        # we assume rules are unique and not infinitely recursive
        # e.g. 'shiny gold bags' contain 3 clear fuchsia bags, <symbol ...>.
        # A => B
        global RULES
        RULES = defaultdict(dict)

        for line in lines:
            # parse rule into unambiguous 'A => B' form
            # keep track of the number of bags possible for each type
            bag = re.match(r'(.*) bags contain', line).groups()[0]
            for count, b in re.findall(r'(\d+) (\w+ \w+) bag', line):
                RULES[bag][b] = int(count)

        global BAG_HOLDERS
        BAG_HOLDERS = set()
        target_bag = 'shiny gold'
        #print(RULES)
        num_bags = find_target(target_bag) - 1

        print(f"Each {target_bag} bag contains {num_bags} other bags")

if __name__ == '__main__':
    main()
