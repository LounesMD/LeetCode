from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        left = root.left  
        right = root.right 

        root.left = None
        root.right = left

        rright = root
        while rright.right:
            rright = rright.right
        rright.right = right
