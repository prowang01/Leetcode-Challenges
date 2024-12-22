# 19. Remove Nth Node From End of List

## Description
Given the `head` of a singly linked list, remove the `n`-th node from the end of the list, and return its head.  

---

### Example 1:

![1](1.jpg)

**Input:**  
`head = [1,2,3,4,5], n = 2`  

**Output:**  
`[1,2,3,5]`

---

### Example 2:

**Input:**  
`head = [1], n = 1`  

**Output:**  
`[]`

---

### Example 3:

**Input:**  
`head = [1,2], n = 1`  

**Output:**  
`[1]`

---

## Constraints:
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`


---

## Approach: Two Pointers with Dummy Node

### Steps:
1. **Create a dummy node**: This simplifies edge cases like removing the head.
2. **Set up two pointers**: Both `fast` and `slow` start at the dummy node.
3. **Move `fast` \(n + 1\) steps forward**: This creates a gap of \(n\) nodes between `fast` and `slow`.
4. **Move both pointers until `fast` reaches the end**: This positions `slow` just before the node to be removed.
5. **Skip the node**: Adjust the `next` pointer of `slow` to skip the target node.
6. **Return the updated list**: Return `dummy.next`, which points to the head of the modified list.

---

## Code:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        for i in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
