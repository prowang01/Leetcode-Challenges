# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to handle edge cases like removing the head
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        for i in range(n+1):
            fast = fast.next
        while fast :
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
        

# Complexity of the algorithm:
# 
# Time: O(n)
# 1. The `for` loop moves `fast` n + 1 steps forward:
#    - O(n) (the constant +1 is negligible for asymptotic complexity).
# 2. The `while fast` loop traverses the rest of the list, which is at most O(n).
#    - Combined, this gives an overall complexity of O(n).
# 
# Space: O(1)
# - The algorithm uses constant auxiliary space for the `dummy`, `fast`, and `slow` pointers.
# - It does not depend on the size of the list.

'''
Runtime : 0 ms
Memory Usage : 17.78 MB

Having done 143. Reorder List previously, this is WAY easier to do and understand.
'''
