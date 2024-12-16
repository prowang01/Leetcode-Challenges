# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach : Using a temporary variable to stock the sub-tree (to inverse after)
# And also using a recursive technique with invertTree().
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:            
            return None

        left = self.invertTree(root.right)
        right = self.invertTree(root.left)

        root.left = left
        root.right = right
        return root


'''
Remember : self already has its two sub-trees inversed, use root instead,
or we'll switch back to the initial state.

invertTree inverses the whole node (sub-tree) and is a recursive function and it calls itself automatically.

Runtime : 0 ms
Memory Usage : 17.49 MB

Temps :

Chaque nœud est visité une fois. Donc, la complexité est O(n), où n est le nombre de nœuds dans l’arbre.

Espace :

La profondeur de la pile d’appels est égale à la hauteur de l’arbre :
O(n) pour un arbre complètement déséquilibré (skewed tree).
O(log(n)) pour un arbre équilibré (balanced tree).

Same reasons as the iterative method, no need to translate.
'''
