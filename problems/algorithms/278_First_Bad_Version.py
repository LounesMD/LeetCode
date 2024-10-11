# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        while left < n:
            middle = left + (n - left) // 2
            if isBadVersion(middle):
                n = middle
            else:
                left = middle + 1
        return left
        