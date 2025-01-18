# 🚀 Problem: Longest Substring Without Repeating Characters

## 📝 Description
Given a string `s`, find the length of the longest substring without repeating characters.

---

## 🔍 Example Test Cases

### Example 1
- **Input**:  
  `s = "abcabcbb"`
- **Output**:  
  `3`
- **Explanation**:  
  The answer is `"abc"`, with the length of 3.

---

### Example 2
- **Input**:  
  `s = "bbbbb"`
- **Output**:  
  `1`
- **Explanation**:  
  The answer is `"b"`, with the length of 1.

---

### Example 3
- **Input**:  
  `s = "pwwkew"`
- **Output**:  
  `3`
- **Explanation**:  
  The answer is `"wke"`, with the length of 3. Notice that the substring must be continuous; `"pwke"` is not valid as it is a subsequence, not a substring.

---

## 💡 Solution Explanation
This problem can be solved efficiently using the sliding window technique:

### Key Steps:
1. Use a **set** to track characters in the current substring.
2. Maintain two pointers:
   - `i`: The start of the current substring.
   - `j`: The end of the current substring, iterating through the string.
3. If the character at `s[j]` is already in the set:
   - Remove characters from the start (`s[i]`) until `s[j]` can be added.
4. Continuously update the maximum length of the substring whenever a new character is added.
5. Return the maximum length after processing the entire string.

### Complexity:
- **Time Complexity**: O(n)  
  Each character is added and removed from the set at most once.
- **Space Complexity**: O(n)  
  The set can hold up to `n` characters in the worst case.

---

## 🧪 Code Implementation
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Initialize a set to store characters in the current substring
        a = set()
        i = 0  # Pointer for the start of the window
        m = 0  # Variable to store the maximum length
        
        # Iterate through the string with the end pointer j
        for j in range(len(s)):
            # If a duplicate character is found
            while s[j] in a:
                # Update the maximum length and shrink the window
                m = max(m, len(a)) 
                a.remove(s[i])  # Remove the start character
                i += 1  # Move the start pointer forward
            # Add the current character to the set
            a.add(s[j])
        
        # Update the maximum length for the last window
        m = max(m, len(a))
        
        return m
