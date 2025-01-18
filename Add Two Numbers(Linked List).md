# 🚀 Problem: Add Two Numbers

## 📝 Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 🔍 Example Test Cases

### Example 1
- **Input**:  
  `l1 = [2,4,3]`  
  `l2 = [5,6,4]`
- **Output**:  
  `[7,0,8]`
- **Explanation**:  
  The numbers represented by the lists are `342` and `465`, and their sum is `807`. Reversing this gives `[7,0,8]`.

---

### Example 2
- **Input**:  
  `l1 = [0]`  
  `l2 = [0]`
- **Output**:  
  `[0]`

---

### Example 3
- **Input**:  
  `l1 = [9,9,9,9,9,9,9]`  
  `l2 = [9,9,9,9]`
- **Output**:  
  `[8,9,9,9,0,0,0,1]`

---

## 💡 Solution Explanation
The solution involves iterating through both linked lists while summing their corresponding digits along with any carry from the previous step. 

### Key Steps:
1. Use a dummy node to simplify the process of building the resultant linked list.
2. Maintain a carry to handle sums greater than or equal to 10.
3. Traverse both linked lists until all nodes are processed, adding corresponding values node by node.
4. Handle any remaining carry after traversal by adding a new node at the end of the result.

The algorithm runs in **O(max(n, m))** time, where `n` and `m` are the lengths of the two linked lists.

---

## 🧪 Code Implementation
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to initialize the result list
        l = ListNode()
        s = l
        c = 0  # Initialize carry as 0
        
        # Traverse both lists simultaneously
        while l1 != None and l2 != None:
            # Sum the values of the current nodes and the carry
            a = (l1.val + l2.val + c)
            c = a // 10  # Update carry
            s.next = ListNode(a % 10)  # Add a new node with the current sum modulo 10
            l1 = l1.next
            l2 = l2.next
            s = s.next
        
        # Process remaining nodes in l1
        while l1 != None:
            a = (l1.val + c)
            c = a // 10
            s.next = ListNode(a % 10)
            s = s.next
            l1 = l1.next
        
        # Process remaining nodes in l2
        while l2 != None:
            a = (l2.val + c)
            c = a // 10
            s.next = ListNode(a % 10)
            s = s.next
            l2 = l2.next
        
        # Add a node for any remaining carry
        if c:
            s.next = ListNode(c)
        
        # Return the next node of the dummy node
        return l.next
