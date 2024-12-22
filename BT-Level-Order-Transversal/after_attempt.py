# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        result = []
        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()         # Removing the first node from the left from queue and assigning the value
                level.append(node.val)         # That's what we'll add to the result : a list
                if node.left:
                    queue.append(node.left)    # We refresh...
                if node.right:
                    queue.append(node.right)   # ... the queue node values
            result.append(level)
        return result

        






'''
Result : a list of list
But we're working with a TreeNode
So let's say we're going to initialize a list and we'll put node values in it.

With some hints, we know that we need to use a queue to manage the 1st and 2nd examples
Level-by-level problem solving

Starting with deque (that functions like a FIFO, first in first out behavior)

Runtime : 0 ms
Memory : 18.38 MB
'''
        