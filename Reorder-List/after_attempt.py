# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Approach : Two Pointers + Reversing and Merging
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: # No nodes or just one node (element)
            return None
        
        # Two pointers to find the middle of the list
        fast, slow = head.next, head
        while fast: # if fast != 0
            fast = fast.next # going to 3 with example 1
            if fast:
                fast = fast.next # going to 4
                slow = slow.next # going to 2

        # Reverse the second part of the list ? 
        prev, curr = None, slow.next
        slow.next = None # End the first list to stop connecting the two lists
        while curr:
            tmp = curr.next
            curr.next = prev  # 4 points to None
            prev = curr       # and None becomes 3
            curr = tmp       # and curr adds 1

        # Merging 
        first, second = head, prev  # starts of the two lists
        while second :
            tmp1, tmp2 = first.next, second.next # next nodes for both
            first.next = second # so the next becomes the second
            second.next = tmp1
            first, second = tmp1, tmp2


# What I learned:
# 1. How to find the middle of a linked list using two pointers (slow and fast).
# 2. How to reverse a linked list using pointers (prev, curr, tmp).
# 3. How to merge two halves of a linked list, one of which is reversed, using iterations.
#
# Challenges faced:
# - Understanding why the initial condition `if not head or not head.next` is critical.
# - Managing pointers properly during the reversal and merging to avoid errors or cycles.
# - Ensuring the linked list is correctly divided into two distinct parts before proceeding.
# - The succesion / order of attributing values to variables is tricky, I have to be careful.

'''
Runtime : 3 ms
Memory Usage : 23.30 MB

Complexity : 

Time : O(n)
1. Traversing the list once for both pointers slow and fast. (O(n))
2. Reversing the list (going through the 2nd half) (O(n))
3. Merging lists (going through all the nodes) (O(n))

Space : O(1)
1. The algorithm is performed in-place, using only constant auxiliary space for the pointers (slow, fast, prev, curr, tmp).

'''
