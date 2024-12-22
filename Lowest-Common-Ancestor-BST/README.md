# 235. Lowest Common Ancestor of a Binary Search Tree

## Description
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

---

## Examples

### Example 1:

![1](1.png)

**Input:**  
`root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`  

**Output:**  
`6`

**Explanation:**  
The LCA of nodes `2` and `8` is `6`.

---

### Example 2:

![1](2.png)

**Input:**  
`root = [6,2,8,0,4,null,null,3,5], p = 2, q = 4`  

**Output:**  
`2`

**Explanation:**  
The LCA of nodes `2` and `4` is `2`, since a node can be a descendant of itself.

---

### Example 3:

**Input Tree:**


**Input:**  
`root = [2,1,3], p = 1, q = 3`  

**Output:**  
`2`

**Explanation:**  
The LCA of nodes `1` and `3` is `2`.

---

## Constraints:
- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`.
- All `Node.val` are unique.
- `p != q`.
- `p` and `q` will exist in the BST.

---

## Approach: Recursive Method

### Steps:
1. **Base case:**  
   - If the root is `None`, return `None`.
   - If the root is equal to `p` or `q`, return the root as it is the LCA.

2. **Compare values:**  
   - If both `p.val` and `q.val` are **less than `root.val`**, search in the left subtree.
   - If both `p.val` and `q.val` are **greater than `root.val`**, search in the right subtree.

3. **Lowest Common Ancestor found:**  
   - If `p.val` is on one side of the root and `q.val` is on the other, return the root as the LCA.

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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

```
---

## Complexity

### Time Complexity:
1. **Traversal of the tree:**
   - In the worst case, we traverse from the root to a leaf, which takes \(O(h)\), where \(h\) is the height of the tree.
   - In a **balanced BST**, \(h = \log(n)\).
   - In a **skewed BST**, \(h = n\).

   **Overall:** **\(O(h)\)**.

---

### Space Complexity:
1. **Recursive stack:**
   - The recursion stack uses \(O(h)\) space in the worst case.

   **Overall:** **\(O(h)\)**.

---

## Notes:
- The recursive approach leverages the BST property to efficiently find the LCA.
- The base case handles when the root is directly one of the nodes (\(p\) or \(q\)).
- The comparison of \(p.val\) and \(q.val\) with \(root.val\) ensures we traverse the correct subtree.

