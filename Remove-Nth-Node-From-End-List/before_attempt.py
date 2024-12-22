# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Approach : Two pointers separated by a 'n' distance
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
            if fast:
                slow = slow.next
        slow.next = slow.next.next

        return dummy.next

'''
didn't work because of 'if fast', this extra verification
'''