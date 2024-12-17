# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach : Recursive Approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
'''
Time Complexity: O(n)

Why?

Each node in the binary tree is visited exactly once.
At every node, we make two recursive calls:
self.maxDepth(root.left)
self.maxDepth(root.right)
Since each recursive call processes a single node, and there are n nodes in total, the time complexity is O(n).

Space Complexity: O(h)

The space complexity depends on the height of the tree because of the recursion stack used during the depth-first traversal.

Worst Case: O(n) (Skewed Tree)
In a skewed tree (like a linked list), all nodes are on one side (either left or right).
The recursion will go as deep as n levels, where n is the total number of nodes.
Hence, the space complexity in this case is O(n).

Best Case: O(log n) (Balanced Tree)
In a balanced binary tree, the height of the tree is approximately log(n) (base 2).
The recursion stack will have at most log(n) function calls, as the tree is symmetrically divided into left and right subtrees.

Hence, the space complexity in this case is O(log n).
'''