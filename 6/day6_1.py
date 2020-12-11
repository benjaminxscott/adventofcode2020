#!/usr/bin/env python3
# https://adventofcode.com/2020/day/6

'''
The form asks a series of 26 yes-or-no questions marked a through z.
All you need to do is identify the questions for which anyone in your group answers "yes".
Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help.
For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z.
(Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input).
Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

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

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
'''

from collections import Counter

def main():
    with open ('day6input.txt') as fp:
        lines = fp.read().splitlines()
        answers = Counter()
        total_answers = 0

        for line in lines:

            if len(line) == 0:
                # we are done processing a block of answers
                #print(f"group_total:{len(answers)}")
                total_answers += len(answers)
                answers = Counter()
            else:
                answers.update(line)
        # hack - to make sure to process the last entry, since otherwise it gets lost as splitlines() doesn't return the final blank line
        total_answers += len(answers)
        print(f"total yes answers: {total_answers}")

if __name__ == '__main__':
    main()
