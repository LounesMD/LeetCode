from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1
            for neighbor in graph[node]:
                if color[neighbor] == 2:
                    continue
                if color[neighbor] == 1 or not dfs(neighbor):
                    return False
            color[node] = 2
            return True

        n = len(graph)
        color = [0] * n
        return [i for i in range(n) if dfs(i)]