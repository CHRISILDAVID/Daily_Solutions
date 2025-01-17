
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
