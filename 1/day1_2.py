#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1#part2

'''
Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''

with open ('day1input.txt') as fp:
    nums = fp.read().splitlines()
    # convert to ints
    nums = [int(x) for x in nums]

    # naive approach
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i == j or j == k or i == k:
                    break
                if nums[i] + nums[j] + nums[k]== 2020:
                    print (nums[i] * nums[j] * nums[k])
