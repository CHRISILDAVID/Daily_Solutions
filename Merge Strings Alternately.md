# Problem: 1768. Merge Strings Alternately
# 
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end 
# of the merged string.
# 
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# 
# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# 
# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for both strings
        i = 0
        j = 0
        # Initialize an empty string to build the result
        s = ""
        
        # Alternate between characters of word1 and word2
        while i < len(word1) and j < len(word2):
            s += word1[i] + word2[j]  # Append one character from each string
            i += 1  # Move to the next character in word1
            j += 1  # Move to the next character in word2
        
        # Append remaining characters from word1 if any
        while i < len(word1):
            s += word1[i]
            i += 1
        
        # Append remaining characters from word2 if any
        while j < len(word2):
            s += word2[j]
            j += 1
        
        return s
