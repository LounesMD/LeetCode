from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkSubTrees(self, left: TreeNode, right: TreeNode):
        if left == None or right == None:
            return left == right
        return left.val == right.val and self.checkSubTrees(left.left, right.right) and self.checkSubTrees(left.right, right.left)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive solution
        """
        if root == None:
            return False
        return self.checkSubTrees(root.left, root.right)
        
sol = Solution()
tree = TreeNode(0, TreeNode(2, TreeNode(3), TreeNode(4)),TreeNode(2, TreeNode(3), TreeNode(4)))
print("res: ", sol.isSymmetric(tree))