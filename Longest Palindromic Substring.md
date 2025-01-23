# 5. Longest Palindromic Substring

---

Given a string s, return the longest palindromic substring in s.

## Example Test Cases

###Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

###Example 2:

Input: s = "cbbd"
Output: "bb"


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ms = s[0]
        def check(l, r): # checks if the current element branches a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)-1): Iterates through the entire string s
            odd = check(i, i)
            even = check(i, i+1)
            if len(odd) > len(ms): # To check if palindrome obtained is larger than earlier 
                ms = odd
            if len(even) > len(ms):
                ms = even
        return ms
