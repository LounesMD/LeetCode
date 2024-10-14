from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Complexity: O(n**2)
        """
        if node == None:
            return None

        historic = dict()
        
        current_nodes = [node]
        
        historic[node.val] = Node(val=node.val)

        for node in current_nodes:

            for neighbor in node.neighbors:

                if neighbor.val not in historic:
                    current_nodes.append(neighbor)

                    historic[neighbor.val] = Node(val=neighbor.val)

                    historic[node.val].neighbors.append(historic[neighbor.val])
                    historic[neighbor.val].neighbors.append(historic[node.val])
                
                elif (neighbor.val in historic) and ( historic[neighbor.val] not in historic[node.val].neighbors):

                    historic[node.val].neighbors.append(historic[neighbor.val])
                    historic[neighbor.val].neighbors.append(historic[node.val])

        return historic[next(iter(historic))]