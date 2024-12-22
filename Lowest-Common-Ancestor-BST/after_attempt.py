# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach : Exploring the 3 possible cases (configurations):
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Case 1 : p on the left side and q on the right side of the node
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        # Case 2 : p or q is the current node (descendant of itself)
        if root.val == p.val or root.val == q.val:
            return root
       # Case 3: Both p and q are in the same subtree
        if p.val < root.val and q.val < root.val:
            # Both p and q are in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            # Both p and q are in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)


'''
Note that for the Binary Search Tree, the left subtree contains the values inferior to the node value,
while the right subtree contains the superior ones.
You have to visualize all the possible configurations by drawing trees or whatever.
Just try to make some things to visualize the problem clearly.


Runtime : 50 ms
Memory : 21.02 MB
'''