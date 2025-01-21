from typing import List 

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        prefix_top = [0] * (n + 1)
        prefix_bottom = [0] * (n + 1)
        
        for i in range(n):
            prefix_top[i + 1] = prefix_top[i] + grid[0][i]
            prefix_bottom[i + 1] = prefix_bottom[i] + grid[1][i]

        min_second_score = float('inf')
        
        for i in range(n):
            top_remaining = prefix_top[n] - prefix_top[i + 1] 
            bottom_remaining = prefix_bottom[i]
            
            second_robot_score = max(top_remaining, bottom_remaining)
            min_second_score = min(min_second_score, second_robot_score)
        
        return min_second_score