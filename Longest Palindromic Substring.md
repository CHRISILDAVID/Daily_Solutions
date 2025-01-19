---

# Longest Palindromic Substring

Title: Given a string `s`, return the longest palindromic substring in `s`.

Description:
Given a string `s`, return the longest substring that reads the same backwards and forwards. For example, "babad" has a longest palindromic substring of "bab", while "cbbd" has a longest palindromic substring of "bb".

Test Cases:

| Input | Output |
| --- | --- |
| "babad" | "bab" |
| "cbbd" | "bb" |
| "aablf" | "aflb" |
| "deadbeef" | "feefdead" |
| "hello world" | "world hello" |

Solution Explanation:
The solution involves iterating through the string character by character, keeping track of the longest palindromic substring encountered so far. The approach is to check if the current character is the same as the previous character, and if it is, then check if the previous character is the same as the next character. If this condition is met, then the current character is part of a palindromic substring, and the longest palindromic substring is updated.

The code example is shown below:
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ms = s[0]
        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)-1):
            odd = check(i, i)
            even = check(i, i+1)

            if len(odd) > len(ms):
                ms = odd
            if len(even) > len(ms):
                ms = even
        
        return ms
```
Additional Insights:

* This problem can be solved using a simple iterative approach, without the need for any additional data structures or complex algorithms.
* The solution relies on the property that if a character is the same as its previous character, then it must be part of a palindromic substring. By keeping track of the longest palindromic substring encountered so far, we can determine the longest palindromic substring in the input string.
* The use of a single `ms` variable to keep track of the longest palindromic substring is a key aspect of the solution. This allows us to efficiently update the longest palindromic substring as we iterate through the input string.
* The code example uses a simple Python implementation, with comments and explanations provided throughout to help understand the solution.
