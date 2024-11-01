from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pp(self, root, res):
        if root == None:
            return
         
        self.pp(root.left, res)
        res.append(root.val)
        self.pp(root.right, res)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []
        self.pp(root, res)
        return res[k-1]