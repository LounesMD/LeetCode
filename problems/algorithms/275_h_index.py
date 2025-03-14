from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1

        while l <= r:
            middle = (l+r)//2

            if (len(citations) - middle) == citations[middle]:
                return citations[middle]

            elif (len(citations) - middle) > citations[middle]:
                l = middle + 1
            else:
                r = middle - 1
                
        return (len(citations) - l)