from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_diameter(self, root, best):
        if root == None:
            return 0 
        left = self.get_diameter(root.left, best)
        right = self.get_diameter(root.right, best)

        best[0] = max(best[0], left+right)

        return 1 +max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = [0]
        self.get_diameter(root, best)
        return best[0]