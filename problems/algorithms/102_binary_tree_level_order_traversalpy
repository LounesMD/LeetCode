from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
        sol, current_nodes, current_order, next_nodes  = [], [root], [], []

        while len(current_nodes) > 0 or len(next_nodes) > 0:
            for node in current_nodes:
                current_order.append(node.val)
                if node.left != None:
                    next_nodes.append(node.left)
                if node.right != None:
                    next_nodes.append(node.right)

            sol.append(current_order)
            current_order = []
            current_nodes = next_nodes
            next_nodes = []

        return sol 