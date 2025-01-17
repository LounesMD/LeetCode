from typing import List 

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        op = 0
        for element in derived:
            op ^= element
        return op == 0