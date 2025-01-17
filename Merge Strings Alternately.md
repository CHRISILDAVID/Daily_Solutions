# Merge Strings Alternately

This repository contains the solution to **LeetCode Problem 1768: Merge Strings Alternately**.

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

### Examples

#### Example 1:
- **Input:** `word1 = "abc"`, `word2 = "pqr"`
- **Output:** `"apbqcr"`
- **Explanation:**

#### Example 2:
- **Input:** `word1 = "ab"`, `word2 = "pqrs"`
- **Output:** `"apbqrs"`
- **Explanation:**

#### Example 3:
- **Input:** `word1 = "abcd"`, `word2 = "pq"`
- **Output:** `"apbqcd"`
- **Explanation:**

---

## Solution

The solution uses two pointers to traverse both strings simultaneously and constructs the merged string. If one string is longer, the remaining characters are appended after the traversal of the shorter string.

### Implementation

The solution is implemented in Python. Below is the code:

```python
class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
      i = 0  # Pointer for word1
      j = 0  # Pointer for word2
      s = ""  # Initialize the result string
      
      # Loop through both strings as long as characters remain in both
      while i < len(word1) and j < len(word2):
          s += word1[i] + word2[j]  # Add one character from each string alternately
          i += 1  # Move pointer in word1
          j += 1  # Move pointer in word2
      
      # If word1 is longer, append the remaining characters
      while i < len(word1):
          s += word1[i]
          i += 1
      
      # If word2 is longer, append the remaining characters
      while j < len(word2):
          s += word2[j]
          j += 1
      
      return s  # Return the final merged string
