#!/usr/bin/env python3
# https://adventofcode.com/2020/day/7

'''
bags must be color-coded and must contain specific quantities of other color-coded bags based on a set of input rules

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag?
(In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

(this seems similar to a context-free grammar, LL parser, ending terminal symbols e.g. 'lambda' )

Answer is something like "how many input symbols will eventually map to a "shiny gold bag" symbol, at some point in its parsing
    We assume that recursive bags aren't possible as part of the ruleset

a => bcc        | light red bags contain 1 bright white bag, 2 muted yellow bags
b => z          |bright white bags contain 1 shiny gold bag
z => terminal   | 1 shiny gold bag contains 1 dark olive bag, 2 vibrant plum bags. (since those symbols go to terminals)

We don't care about parsing all the way to 'terminal', since the only thing that matters is if we can get to 'z' from input symbol
'''

def find_target(rule, target):
    found = False
    # if found or terminal, return back up the stack
    if target in rule:
        #print("found")
        found = True
    else:
        print(f"checking {rule}")
        for next_rule in RULES.get(rule):
            found = find_target (next_rule, target)

    return found

def main():
    with open ('day7input.txt') as fp:
        lines = fp.read().splitlines()
        # symbols always have two adjectives, numbers don't matter
        # we assume rules are unique and not infinitely recursive
        # e.g. 'shiny gold bags' contain 3 clear fuchsia bags, <symbol ...>.
        # A => B
        global RULES
        RULES = {}

        for line in lines:
            # parse rule into unambiguous 'A => B' form

            insymbol, outsymbols = line.split(' bags contain ')
            outsymbols = outsymbols.split(', ')
            outsymbols = [x.strip('.') for x in outsymbols]
            outsymbols = [x.split(' bag')[0] for x in outsymbols]
            outsymbols = [' '.join(x.split(' ')[1:]) for x in outsymbols]

            # save off rule
            RULES.update({insymbol:outsymbols})

        # 'other' implies terminal symbol
        RULES.update({'other':[]})

        bag_holders = 0
        target_bag = 'shiny gold'
        print(RULES)
        for leftside, rightside in RULES.items():
            print(f"evaluating: {leftside} => {rightside}")
            for rule in rightside:
                if find_target(rule, target_bag):
                    bag_holders +=1
                    break

        print(f"outermost bags that can hold {target_bag}: {bag_holders}")
if __name__ == '__main__':
    main()
