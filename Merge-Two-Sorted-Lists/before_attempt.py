# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        final = []

        while current1 :
            final = current1
            next_node1 = current1.next
            final.next = next_node1
        while current2 :
            final = current2
            next_node2 = current2.next
            final.next = next_node2
        return final
             
        
'''
Just a before attempt because I didn't have any idea to solve this problem.
'''