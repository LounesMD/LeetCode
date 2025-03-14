class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while True:   
            s = numbers[l] + numbers[r]         
            if s == target:
                return [l+1,r+1]
            elif s > target:
                r -= 1
            else:
                l += 1               
        return None

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            if new_target in t:
                return [ t[new_target] , i + 1]
            t[numbers[i]] = i  + 1
        return None