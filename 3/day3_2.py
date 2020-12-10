#!/usr/bin/env python3
# https://adventofcode.com/2020/day/3#part2

'''
Determine the number of trees you would encounter if, for each of the following slopes,
you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

'''

def main():
    with open ('day3input.txt') as fp:
        # the first line doesn't matter since we can't hit any trees there
        lines = fp.read().splitlines()[1:]
        # we assume the slope sections are a constant width
        mountain_width = len(lines[0])
        slopes = [
            {'right':1,'down':1},
            {'right':3,'down':1},
            {'right':5,'down':1},
            {'right':7,'down':1},
            {'right':1,'down':2},
        ]

        total_trees_hit = 1

        for slope_num, slope in enumerate(slopes):
            num_trees_hit = 0
            skifree = 0
            for line_index, line in enumerate(lines):
                # skip lines to handle the "go down multiple times" case
                if (slope.get('down') > 1) and (line_index % slope.get('down') == 0):
                    continue
                skifree += slope.get('right')
                # we modulo the index so if we get to the edge we loop back around
                #print(f"line {line_index} was a {line[skifree % mountain_width]}")
                if line[skifree % mountain_width] == '#':
                    # we have hit a tree
                    num_trees_hit += 1
            total_trees_hit *= num_trees_hit
            print(f"Run #{slope_num}: {num_trees_hit} trees hit for slope: {slope}")
        print (f"total:{total_trees_hit}")

if __name__ == '__main__':
    main()
