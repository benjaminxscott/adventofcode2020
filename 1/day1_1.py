#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1

'''
From newline delimited input, find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Find the two entries that sum to 2020; what do you get if you multiply them together?
'''



def find_sums(filepath:str) -> None:
    with open (filepath) as fp:
        nums = fp.read().splitlines()
        # convert to ints
        nums = [int(x) for x in nums]

        # naive approach
        found = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                #print (f"comparing {i} and {j} with sum {nums[i] + nums[j]}")
                #print (f"comparing {nums[i]} and {nums[j]}")
                if not found and sum([nums[i],nums[j]]) == 2020:
                    print (nums[i] * nums[j])
                    found = True

if __name__ == '__main__':
    find_sums (filepath = 'day1input.txt')