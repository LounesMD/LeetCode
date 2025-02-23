from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or postorder == []:
            return None


        if len(preorder) == 1:
            return TreeNode(preorder[0])

        left_root_val = preorder[1]
        left_subtree_size = postorder.index(left_root_val) + 1

        left_preorder = preorder[1:left_subtree_size + 1]
        left_postorder = postorder[:left_subtree_size]

        right_preorder = preorder[left_subtree_size + 1:]
        right_postorder = postorder[left_subtree_size:-1]

        return TreeNode(
            val= preorder[0],
            left= self.constructFromPrePost(left_preorder, left_postorder),
            right= self.constructFromPrePost(right_preorder, right_postorder),
        )