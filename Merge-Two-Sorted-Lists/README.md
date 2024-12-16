# 21. Merge Two Sorted Lists

## Description
Merge two sorted linked lists into one sorted linked list. The resulting list should also be sorted.

### Example 1:

![1](1.jpg)

**Input:**  
list1 = [1,2,4], list2 = [1,3,4]  
**Output:**  
[1,1,2,3,4,4]

### Example 2:

**Input:**  
list1 = [], list2 = []  
**Output:**  
[]

### Example 3:

**Input:**  
list1 = [], list2 = [0]  
**Output:**  
[0]

---

## Constraints:
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`.
- Both `list1` and `list2` are sorted in non-decreasing order.

---

## Approach: Two Pointers

We use the **Two Pointers** technique to traverse both lists simultaneously, merging them node by node. The dummy node simplifies the merging process by eliminating edge cases for the first node.

---

## Steps:
1. Create a dummy node to simplify the process of merging.
2. Use a pointer (`cur`) to track the current node in the merged list.
3. Compare the values of the current nodes in `list1` and `list2`.
   - Add the smaller node to the merged list and move the pointer forward in the respective list.
4. Once one of the lists is exhausted, link the remaining nodes of the other list directly.
5. Return `dummy.next`, which skips the dummy node and points to the merged list.

---

## Code:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return dummy.next

```

---

## Complexity
- **Runtime:**  
  0 ms
- **Memory Usage:**  
  17.42 MB

### Time Complexity:
1. n is the number of nodes in list1.
2. m is the number of nodes in list2.

The algorithm iterates through both lists exactly once, comparing and adding nodes until one of the lists is empty.
After the loop, the remaining nodes of the non-empty list (if any) are linked in O(1), as no additional traversal is needed.

**Overall:** **O(n+m)**.

### Space Complexity:
1. The algorithm operates directly on the input linked lists without using any additional data structures.
2. Only a few pointers (dummy, cur, list1, list2) are used for tracking the current nodes, which take constant space.
**Overall:** **O(1)**.


# Notes:
This implementation differs from the typical Two Pointers technique, as both pointers (list1 and list2) traverse the beginnings of their respective lists. Unlike other problems where one pointer starts at the beginning and another at the end, here both pointers move linearly from the start of their lists.