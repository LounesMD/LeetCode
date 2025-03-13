from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [1,1]
        
        for _ in range(1,rowIndex):
            curr = [1]
            for i in range(len(prev)-1):
                curr.append(prev[i]+prev[i+1])
            curr.append(1)
            prev = curr
        return prev