# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach : Using a temporary variable to stock the sub-tree (to inverse after)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root:
            while root.left :
                temp = root.left
                root.left = root.right
                root.right = temp 
        return root


# Intuition may be good : but technical skills about binary trees is bad
# Need more understanding about this concept too.

        