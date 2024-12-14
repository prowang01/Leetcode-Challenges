# 206. Reverse Linked List

## Description
Given the head of a singly linked list, reverse the list, and return the reversed list.

### Example 1:

![1](Example1.jpg)

**Input:** head = [1,2,3,4,5]  
**Output:** [5,4,3,2,1]

### Example 2:

![2](Example2.jpg)

**Input:** head = [1,2]  
**Output:** [2,1]

### Example 3:
**Input:** head = []  
**Output:** []

### Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000.

---

## Approach
**Iterative Two-Pointer Technique:**  
1. Use two pointers: `prev` and `current`.  
   - `prev` starts as `None`.  
   - `current` starts as the `head` of the list.  
2. Iterate through the list:  
   - Save the next node in a temporary variable `next_node`.  
   - Reverse the link of `current` by pointing it to `prev`.  
   - Move `prev` to `current` and `current` to `next_node`.  
3. Once the list is fully traversed, `prev` will be the new head of the reversed list.

---

## Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        # Iteratively reverse the linked list
        while current:
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        return prev  # New head of the reversed list
```

## Complexity
- **Runtime:**  
  0 ms
- **Memory Usage:**  
  18.31 MB

### Time Complexity:
1. The solution traverses the linked list once, which is O(n), where n is the number of nodes in the linked list.
**Overall:** **O(n)**.

### Space Complexity:
1. The solution uses a constant amount of extra space for pointers (prev, current, next_node), so the space complexity is O(1).
**Overall:** **O(1)**.


# Notes:
This solution relies on understanding how pointers work in a linked list.
By reversing the next pointers in each node iteratively, the entire list is reversed.
Visualizing the changes in the pointers step by step can help greatly in understanding this algorithm.
