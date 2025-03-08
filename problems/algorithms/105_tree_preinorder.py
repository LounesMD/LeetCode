# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root = preorder[0]

        if len(preorder) == 1:
            return TreeNode(val=root)

        idx = inorder.index(root)

        return TreeNode(
            val = root,
            left=self.buildTree(
                preorder[1:1+idx],
                inorder[:idx],
            ),
            right=self.buildTree(
                preorder[1+idx:],
                inorder[idx+1:],
            )
        )