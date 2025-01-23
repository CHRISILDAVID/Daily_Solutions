# 1. Two Sum

---

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


## Example Test Cases

### Example 1
- **Input**: `nums = [2,7,11,15], target = 9`
- **Output**: `[0,1]`
- **Explanation**: `nums[0] + nums[1] == 9`, so the result is `[0, 1]`.

### Example 2
- **Input**: `nums = [3,2,4], target = 6`
- **Output**: `[1,2]`
- **Explanation**: `nums[1] + nums[2] == 6`, so the result is `[1, 2]`.

### Example 3
- **Input**: `nums = [3,3], target = 6`
- **Output**: `[0,1]`
- **Explanation**: `nums[0] + nums[1] == 6`, so the result is `[0, 1]`.

---

## Solution
```python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums): # iterate the array and add all the values as keys and their index positions as values of the dictionary "s" until the complement of the target when subtracted with the current element of the array is found in s
            diff = target - n
            if diff in s:
                return [s[diff], i]
            s[n] = i
