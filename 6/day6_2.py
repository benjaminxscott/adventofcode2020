#!/usr/bin/env python3
# https://adventofcode.com/2020/day/6

'''
You don't need to identify the questions to which anyone answered "yes";
you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?


'''

from collections import Counter

def main():
    with open ('day6input.txt') as fp:
        lines = fp.read().splitlines()
        answers = Counter({'participants':0})
        total_answers = 0

        for line in lines:

            if len(line) == 0:
                # we are done processing a block of answers
                #print(f"group_total:{len(answers)}")
                total_answers += len([x for x in answers if answers[x] == answers['participants'] and x is not 'participants'])
                answers = Counter({'participants':0})
            else:
                answers.update(line)
                answers.update({'participants'})

        # hack - to make sure to process the last entry, since otherwise it gets lost as splitlines() doesn't return the final blank line
        total_answers += len([x for x in answers if answers[x] == answers['participants'] and x is not 'participants'])
        print(f"total yes answers: {total_answers}")

if __name__ == '__main__':
    main()
