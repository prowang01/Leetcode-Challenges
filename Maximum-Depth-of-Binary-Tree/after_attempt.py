# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach : using a stack again (see Invert Binary Tree problem) to check all the nodes
# and using a variable max_depth to return the depth
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0

        stack = [(root,1)]
        max_depth = 0

        while stack :
            node, depth = stack.pop()
            if node :
                max_depth = max(max_depth, depth)
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
        return max_depth
        
'''
Here, the stack is a tuple (node.val, depth).
So it's the same process, we take the last element of the stack,
We check if there are children,
And in the case children exist, we add 1 to the depth and we add the child to the stack.
In the .append() method, don't forget extra parentheses to precise the fact that the object is a tuple.

Runtime : 0 ms
Memory : 19.12 MB

Complexity : we go through the nodes only once, so n nodes
We also have a constant variable that is max_depth,
so maybe O(n) ?


Time Complexity :
The time complexity is O(n), where n is the total number of nodes in the tree.

Why ?

Each node in the tree is visited exactly once.
At each node:
We check for its children (left and right) and update the depth accordingly.
This work (comparing and adding to a stack) takes constant time O(1).
Since we visit every node once and only once, the total time complexity is proportional to the number of nodes: O(n).

Space Complexity : 
The space complexity depends on the height of the tree, which determines the maximum size of the explicit stack (in the iterative approach).

1. Worst Case (Skewed Tree): O(n)
If the tree is skewed, all nodes lie along one side (like a linked list).
The height of the tree 
ℎ is equal to 𝑛 (the total number of nodes).

In this case:
The explicit stack will store n nodes.
Space Complexity: O(n).


There is no before_attempt because I couldn't find an answer.
'''