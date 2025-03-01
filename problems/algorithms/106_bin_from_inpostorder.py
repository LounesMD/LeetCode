# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        root = postorder[-1]

        if len(postorder) == 1:
            return TreeNode(val=root)
        idx = inorder.index(root)
        nb_elt_right = len(inorder) - (idx + 1)

        return TreeNode(val = root, left=self.buildTree(inorder[: idx ], postorder[:len(postorder) - nb_elt_right - 1]) , right=self.buildTree(inorder[idx + 1: ], postorder[-nb_elt_right-1:-1]))        