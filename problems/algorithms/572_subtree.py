from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def same(self, a, b):
        if a is None or b is None:
            return a == None and b == None

        elif a.val == b.val:
            return self.same(a.left, b.left) and self.same(a.right, b.right)
        
        return False 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True 
        
        elif root == None:
            return False
        
        if self.same(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)