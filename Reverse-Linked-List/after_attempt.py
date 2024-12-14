# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
          
        return prev


'''
Runtime : 0 ms
Memory Usage : 18.31 MB

After trial and error, I've finally understood the concept of linked lists,
The links between the nodes are important, that's why we're playing / manipulating
the '2' variables prev, current, and the method .next carefully.
Using a drawing is very beneficial to understand the problem.


Time complexity:

The time complexity of this solution is O(n), because we reversed the linked list in a single pass, where 𝑛 n is the number of nodes in a linked list.

Space complexity:

The space complexity of this solution is O(1), because no extra memory is used.

'''