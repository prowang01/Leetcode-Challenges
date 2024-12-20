# 143. Reorder List

## Description
You are given the head of a singly linked list. The list can be represented as:  

`L₀ → L₁ → ... → Lₙ₋₁ → Lₙ`

Reorder the list to be in the following form:  

`L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → ...`

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
---

## Examples

### Example 1:

![1](1.jpg)

**Input List:**  
`1 → 2 → 3 → 4 → 5`

**Output List:**  
`1 → 5 → 2 → 4 → 3`

---

### Example 2:

![1](2.jpg)

**Input List:**  
`1 → 2 → 3 → 4`

**Output List:**  
`1 → 4 → 2 → 3`


---

## Constraints:
- The number of nodes in the list is in the range `[1, 10^5]`.
- `-1000 <= Node.val <= 1000`.

---

## Approach: Two Pointers + Reversing and Merging

### Steps:
1. **Edge Case:** If the list is empty or has only one node, return the list as-is.
2. **Find the middle of the list:**  
   Use two pointers (`slow` and `fast`) to find the midpoint.
3. **Reverse the second half of the list:**  
   Reverse the nodes in the second half of the list using a pointer-based approach.
4. **Merge the two halves:**  
   Interleave nodes from the first and second halves to achieve the desired order.

---

## Code:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        
        # Find the middle of the list
        fast, slow = head.next, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        # Reverse the second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

```

---

## Complexity
- **Runtime:**  
  3 ms
- **Memory Usage:**  
  23.30 MB

### Time Complexity:
1. Finding the middle: 𝑂(𝑛)
2. Reversing the second half: 𝑂(𝑛/2) =𝑂(𝑛)
3. Merging the two halves: 𝑂(𝑛)

**Overall:** **O(n)**.

### Space Complexity:
1. The algorithm is in-place and uses only constant extra space for pointers (slow, fast, prev, curr, etc.).

**Overall:** **O(1)**.

# Notes:
1. Why reverse the second half? This simplifies merging by providing direct access to the nodes from the end of the original list.
2. Edge cases handled: Empty list, single node, even and odd number of nodes.
3. Pointers: Proper pointer management is key to avoiding cycles or segmentation faults.