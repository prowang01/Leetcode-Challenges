# 104. Maximum Depth of Binary Tree

## Description
Given the `root` of a binary tree, return its **maximum depth**.

The **maximum depth** is defined as the number of edges on the longest path from the root to a leaf node.  
An empty tree has a depth of `0`.

---

## Examples

### **Example 1**

**Input Tree:**

![1](1.jpg)

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** `3`  

---

### **Example 2**

**Input:** root = [2,1,3]  
**Output:** `2`

---

### **Example 3**

**Input:** `[]` (empty tree)  
**Output:** `0`

---

## Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`.

---

```python
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

```
---

## **Approach 1: Iterative Depth-First Search (DFS) Using a Stack**

### Steps:
1. **Base case:**
   - If the root is `None` (empty tree), the depth is `0`.
2. **Initialize a stack:**
   - Use a stack to store tuples containing the current node and its depth.
   - Start with the root node and an initial depth of `1`.
3. **Depth-First Traversal:**
   - While the stack is not empty:
     - Pop the current node and its depth.
     - Update the maximum depth if the current depth is greater.
     - If the left child exists, add it to the stack with `depth + 1`.
     - If the right child exists, add it to the stack with `depth + 1`.
4. **Return the maximum depth:**
   - Once all nodes have been processed, return the maximum depth.

---

## **Code 1**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # Base case: If tree is empty
            return 0

        stack = [(root, 1)]  # Initialize the stack with the root and depth 1
        max_depth = 0  # To store the maximum depth

        while stack:  # While there are nodes to process
            node, depth = stack.pop()  # Get the current node and its depth
            if node:  # If the node exists
                max_depth = max(max_depth, depth)  # Update maximum depth
                if node.left:  # Add the left child to the stack
                    stack.append((node.left, depth + 1))
                if node.right:  # Add the right child to the stack
                    stack.append((node.right, depth + 1))

        return max_depth  # Return the maximum depth

```

## Complexity
- **Runtime:**  
  0 ms
- **Memory Usage:**  
  19.12 MB

### Time Complexity:
O(n)

### Space Complexity:
1. O(h), where h is the height of the tree.
2. In the worst case (skewed tree), h = n, so O(n).
3. In the best case (balanced tree), h = log(n), so O(log(n)).
**Overall:** **Depends**.


---


## Approach 2 : Recursive Depth-First Search (DFS)

### Steps:
1. **Base case:**  
   - If the root is `None` (empty tree), the depth is `0`.
2. **Recursive calls:**  
   - Call `maxDepth` on the left child: `self.maxDepth(root.left)`.
   - Call `maxDepth` on the right child: `self.maxDepth(root.right)`.
3. **Combine results:**  
   - Take the maximum depth between the left and right subtrees and add `1` to account for the current node.
4. Return the result.

---

## Code 2 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

Same complexity as in Approach 1