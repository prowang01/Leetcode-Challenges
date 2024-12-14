# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = head[::-1]
        return reversed_list
        


'''
Approach : using the simple list concept, which is totally wrong.
We're here in the linked list, which functions with nodes and head and values etc.

'''
