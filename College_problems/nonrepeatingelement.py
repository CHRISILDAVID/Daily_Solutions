"""
Given a non-empty array of integers nums, every element appears twice except for one. Find
that single one.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

def nonrepeatingelement(nums):
    freq_map = {}
    for i in nums: # add elements along with their frequency to freq_map
        if i not in freq_map:
            freq_map[i] = 1
        else:
            freq_map[i]+=1
    for i in freq_map: # iterate freq_map to find the element with frequency 1
        if freq_map[i] == 1:
            return i
    return -1

print(nonrepeatingelement([2,2,1]))