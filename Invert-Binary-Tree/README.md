# 226. Invert Binary Tree

## Description
Given the `root` of a binary tree, invert the tree, and return its `root`.

---

## Examples

### Example 1:

**Input Tree:**

![1](1.jpg)


**Input:** root = [4,2,7,1,3,6,9]  
**Output:** [4,7,2,9,6,3,1]

---

### Example 2:

**Input Tree:**

![1](2.jpg)

**Output Tree:**



**Input:** root = [2,1,3]  
**Output:** [2,3,1]

---

### Example 3:

**Input :**  root = `[]`


**Output :**  `[]`
---

## Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`.

---

## Approach: Using a Stack (Iterative Method)

### Steps:
1. **Edge case:** If the root is `None`, return `None`.
2. **Initialize a stack:** Start with the root node in the stack.
3. **While the stack is not empty:**
   - Pop the current node from the stack.
   - Swap its left and right children.
   - If the left child exists, add it to the stack.
   - If the right child exists, add it to the stack.
4. Once the entire tree is processed, return the root.

---

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  
            return None

        stack = [root]  
        while stack:
            node = stack.pop() 
            
            
            node.left, node.right = node.right, node.left

            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root  

```


## Complexity
- **Runtime:**  
  0 ms
- **Memory Usage:**  
  17.45 MB

### Time Complexity:
1. O(n), where n is the total number of nodes in the tree.
2. Each node is processed exactly once.
**Overall:** **O(n)**.

### Space Complexity:
1. O(h), where h is the height of the tree.
2. In the worst case (skewed tree), h = n, so O(n).
3. In the best case (balanced tree), h = log(n), so O(log(n)).
**Overall:** **Depends**.


# Notes:
Stack Behavior: The stack stores nodes to be processed. Each node's children (`left` and `right`) are added explicitly.
Why Iterative ? This avoids recursion depth issues for deeply skewed trees.
Order of processing: Nodes are processed one by one, and children are added in left-to-right order.
