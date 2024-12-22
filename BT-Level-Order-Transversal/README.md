# 102. Binary Tree Level Order Traversal

## Description
Given the `root` of a binary tree, return the level order traversal of its nodes' values.  
(i.e., from left to right, level by level).

---

## Examples

### Example 1:
![1](1.jpg)

**Input:**  
`root = [3,9,20,null,null,15,7]`

**Output:**  
`[[3],[9,20],[15,7]]`

---

### Example 2:
**Input:**  
`root = [1]`

**Output:**  
`[[1]]`

---

### Example 3:
**Input:**  
`root = []`

**Output:**  
`[]`

---

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`.

---

## Approach: Using a Queue (Breadth-First Search)

### Steps:
1. **Handle edge case:**  
   - If the tree is empty (`root = None`), return an empty list: `[]`.

2. **Use a queue for BFS traversal:**  
   - Initialize the queue with the root node: `deque([root])`.
   - Process nodes level by level.

3. **For each level:**
   - Determine the number of nodes in the current level using `len(queue)`.
   - Process each node in the level:
     - Remove the node from the queue.
     - Append its value to the current level's list.
     - Add the node's left and right children to the queue (if they exist).
   - Append the current level's list to the result.

4. **Return the result:**  
   - After processing all levels, return the list of lists.

---

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handle empty tree
        if not root:
            return []
        
        # Initialize result and queue
        result = []  # Final list of levels
        queue = deque([root])  # Start with root node in the queue
        
        while queue:  # Process while there are nodes in the queue
            level = []  # Store all values in the current level
            for _ in range(len(queue)):  # Iterate through the current level's nodes
                node = queue.popleft()  # Remove the first node from the queue
                level.append(node.val)  # Add its value to the level list
                if node.left:  # Add left child if it exists
                    queue.append(node.left)
                if node.right:  # Add right child if it exists
                    queue.append(node.right)
            result.append(level)  # Add the current level to the result
        
        return result

```

## Complexity

### Time Complexity:
The key operations in the algorithm are:

1. **Visiting Each Node Once:**
   - Every node is processed exactly once (when dequeued).
   - With \(n\) nodes in the tree, this operation takes:
   \[
   O(n)
   \]

2. **Adding Nodes to the Queue:**
   - For each node, its children are enqueued (left and right).
   - Each node is added to the queue exactly once, which also takes:
   \[
   O(n)
   \]

**Overall Time Complexity:**  
Both visiting nodes and adding them to the queue are linear operations. Hence, the total time complexity is:
\[
O(n)
\]

---

### Space Complexity:
The space complexity depends on the maximum size of the queue:

1. **Worst Case - Perfectly Balanced Tree:**
   - In a balanced binary tree, the last level can have up to \(\frac{n}{2}\) nodes (where \(n\) is the total number of nodes).
   - At most, the queue holds all nodes in the last level, so:
   \[
   O(n)
   \]

2. **Best Case - Skewed Tree:**
   - In a completely skewed tree (like a linked list), the queue holds at most one node at any time:
   \[
   O(1)
   \]

3. **No Recursive Stack:**
   - The algorithm doesn’t use recursion, so there’s no extra space used for a recursive stack.

**Overall Space Complexity:**  
\[
O(n)
\]
(in the worst case, where the last level contains half of all nodes).

---

### Notes:
1. The **queue** dynamically adjusts as nodes are added and removed, ensuring efficient level-by-level traversal.
2. A `deque` is used for \(O(1)\) operations when adding or removing nodes.
3. The algorithm avoids recursion to reduce memory overhead, making it suitable for large trees.
