# 🚀 Problem: Two Sum

## 📝 Description
Given an array of integers `nums` and an integer `target`, the task is to find two distinct indices in the array such that the numbers at these indices add up to the `target`. You may assume that each input would have exactly one solution, and the same element cannot be used twice.

You can return the answer in **any order**.

---

## 🔍 Example Test Cases

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

## 💡 Solution Explanation
The solution utilizes a **hash map (dictionary)** for efficient lookups. Here's the step-by-step breakdown:

1. Initialize an empty dictionary `s` to store numbers and their indices.
2. Iterate through the array `nums`:
   - Calculate the difference between `target` and the current number, `diff = target - n`.
   - Check if `diff` exists in the dictionary:
     - If yes, return the indices `[s[diff], i]` as the solution.
   - Otherwise, store the current number `n` along with its index `i` in the dictionary.
3. Since the problem guarantees one solution, the function will always return valid indices.

This approach ensures that each number is processed only once, resulting in a time complexity of **O(n)**.

---

## 🧪 Code Implementation
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store seen numbers and their indices
        s = {}
        # Iterate through the array with indices
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n
            # Check if the difference is already in the dictionary
            if diff in s:
                # Return the indices of the two numbers
                return [s[diff], i]
            # Store the current number with its index
            s[n] = i
