# Approach : Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()   # Create a new linked lsit
        while list1 and list2 : # Les 2 en même temps ? 
            if list1.val < list2.val : 
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else : 
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next 

'''
Problem 1 : We have an extra 0 in the start of the list
Using the dummy node, we don't need to solve the case : if the merged linked list is not empty.
We just create the chain and then skip the first one (dummy)

Problem 2 : When two lists aren't of the same length,
We just link the list that isn't empty directly after the merged one because it takes all the remaining nodes.
All nodes are linked, that's why.

Runtime : 0 ms
Memory Usage : 17.42 MB

Time Complexity : 

The time complexity of merging two sorted linked lists is O(n + m), where:

n is the number of nodes in list1.
m is the number of nodes in list2.

Explanation:
The algorithm iterates through both lists exactly once, comparing and adding nodes until one of the lists is empty.
After the loop, the remaining nodes of the non-empty list (if any) are linked in O(1), as no additional traversal is needed.

Space Complexity : 

The space complexity is O(1).

Explanation:

The algorithm operates directly on the input linked lists without using any additional data structures.
Only a few pointers (dummy, cur, list1, list2) are used for tracking the current nodes, which take constant space.

Summary : 

Time Complexity: O(n + m) (linear in the total number of nodes in both lists).
Space Complexity: O(1) (constant additional space, as no new list is created).
'''
        