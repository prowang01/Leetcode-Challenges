# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach : Using a stack technique (iterative method).
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:            # In case when root has nothing.
            return None

        stack = [root]  # Initializing the stack with the root node (ex 1 = '4')
        while stack:
            node = stack.pop() # Kicking out the node from root and retrieving the node to the 'node' variable (in our case : 4)
            node.left, node.right = node.right, node.left

            if node.left:        # Adding child nodes (if existing)
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


'''
Remember : We always add nodes from up to down, left to right,
Here in the first example, 
We always go from left to right with append, so we can add 7 then 2 with the inversed nodes.

Besides, talking about stack.pop(), it retrieves the NODE, which may contain the children.
And then delete the node from the stack.
So for the 1st iteration, stack contains nothing. 

The stack contains only the nodes, we can get the children with the .left and .right methods.

Runtime : 0 ms
Memory usage : 17.45 MB


Time Complexity : 

The time complexity of inverting a binary tree is O(n), where n is the total number of nodes in the tree.

Explanation:

Each node in the tree is visited exactly once.
During the traversal, for each node, we perform a constant amount of work (swapping its left and right children and adding them to the stack if they exist).
Therefore, the total time taken is proportional to the number of nodes, O(n).

Space Complexity : 

The space complexity depends on the method of traversal and the structure of the tree:

1. Iterative Approach (using a stack):

The space complexity is O(h), where h is the height of the tree.

In the worst case:

For a completely skewed tree (like a linked list), h = n, so the space complexity is O(n).
For a balanced binary tree, h = log(n), so the space complexity is O(log(n)).

Summary : 

Time Complexity: O(n) (every node is processed once).
Space Complexity: O(h) (height of the tree).

Worst case: O(n) for a skewed tree.
Best case: O(log(n)) for a balanced tree.

'''
